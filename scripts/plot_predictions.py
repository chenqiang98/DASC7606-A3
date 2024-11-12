from matplotlib import pyplot as plt
from get_accuracy import get_accuracy_and_confidence_table

col1 = (20, 54, 95)
col2 = (118, 162, 185)
col3 = (191, 217, 229)
col4 = (248, 242, 236)
col5 = (214, 79, 56)

# color to plt
col1 = [c / 255 for c in col1]
col2 = [c / 255 for c in col2]
col3 = [c / 255 for c in col3]
col4 = [c / 255 for c in col4]
col5 = [c / 255 for c in col5]

# col1 is too light, change to col2
col1_ = col1
col1 = col2

# fontsize
fsize_text = 15
fsize_title = 16

# fonttype
# plt.rcParams['font.family'] = 'Arial'
# print(plt.rcParams['font.family']) # 'sans-serif'
fonttype = 'Arial'

def plot_predictions(json_fpath):
    fig, ax = plt.subplots()
    _, confidence_counter, confidence_correct_counter = get_accuracy_and_confidence_table(json_fpath)
    confidence = sorted(confidence_counter.keys())
    # str_confidence = [str(c*16) for c in confidence]
    # str_confidence in fraction
    str_confidence = [f'{int(c*16)}/16' for c in confidence]
    correct = [confidence_correct_counter[c] for c in confidence]
    total = [confidence_counter[c] for c in confidence]
    conf_counts = {
        'total': total,
        'correct': correct,
    }
    acc_rate = [c / t if t != 0 else 0 for c, t in zip(correct, total)]
    # acc_rate in percentage
    acc_rate = [r * 100 for r in acc_rate]
    for label, counts in conf_counts.items():
        # print(label, counts)
        p = ax.bar(str_confidence, counts, width=0.6, label=label, color=col3 if label == 'total' else col1)
        # if counts
        if hasattr(ax, 'bar_label'):
            if label == 'total':
                ax.bar_label(p, label_type='edge')
            else:
                ax.bar_label(p, label_type='center')
    ax.set_ylabel('Counts', color=col1_, fontdict={'fontsize':fsize_text})
    ax.set_xlabel('Confidence(16 forward passes)', fontdict={'fontsize':fsize_text})
    ax.legend(['Total', 'Correct'], loc='upper left')
    ax.set_title('t=0.6, 1B', fontdict={'fontsize':fsize_title})
    ax2 = ax.twinx()
    # plot with percentage in y-axis
    ax2.plot(str_confidence, acc_rate, color=col5, marker='o')
    ax2.set_ylabel('Accuracy Rate (%)', color=col5, fontdict={'fontsize':fsize_text})
    ax2.set_ylim(20, 90)
    # ax2.legend(['Accuracy Rate'], loc='upper left')

    # show overall accuracy rate
    accuracy = sum(correct) / sum(total)
    accuracy = accuracy * 100
    ax2.axhline(y=accuracy, color=col2, linestyle='--')
    ax2.text(11.9, accuracy, f'Overall Accuracy {accuracy:.2f}%', color=col1_, ha='right')
    
    # set picture size
    fig.set_size_inches(12, 3)

    fig.set_dpi(500.0)

    # plt.show()

    fig.savefig('report/Figures/plot_prediction.png')


def plot_predictions_2x2(json_fpath_list):
    '''
    Plot in 2x2 grid.
    '''
    description = ['t=0.6, 1B',
                   't=1.0, 1B',
                   't=0.2, 1B',
                   't=0.6, 3B']
    fig, axs = plt.subplots(2, 2)
    max_acc_rate = 0
    for json_fpath in json_fpath_list:
        _, confidence_counter, confidence_correct_counter = get_accuracy_and_confidence_table(json_fpath)
        correct = [confidence_correct_counter[c] for c in sorted(confidence_counter.keys())]
        total = [confidence_counter[c] for c in sorted(confidence_counter.keys())]
        acc_rate = [c / t if t != 0 else 0 for c, t in zip(correct, total)]
        acc_rate = [r * 100 for r in acc_rate]
        max_acc_rate = max(max_acc_rate, max(acc_rate))

    for i, json_fpath in enumerate(json_fpath_list):
        ax = axs[i // 2, i % 2]
        _, confidence_counter, confidence_correct_counter = get_accuracy_and_confidence_table(json_fpath)
        confidence = sorted(confidence_counter.keys())
        # str_confidence = [str(c) for c in confidence]
        str_confidence = [f'{int(c*8)}/8' for c in confidence]
        correct = [confidence_correct_counter[c] for c in confidence]
        total = [confidence_counter[c] for c in confidence]
        conf_counts = {
            'total': total,
            'correct': correct,
        }
        acc_rate = [c / t if t != 0 else 0 for c, t in zip(correct, total)]
        acc_rate = [r * 100 for r in acc_rate]
        for label, counts in conf_counts.items():
            p = ax.bar(str_confidence, counts, width=0.6, label=label, color=col3 if label == 'total' else col1)
            if hasattr(ax, 'bar_label'):
                if label == 'total':
                    ax.bar_label(p, label_type='edge')
                else:
                    ax.bar_label(p, label_type='center')
        # ax.set_ylabel('Count')
        # ax.set_xlabel('Confidence')
        if i==0:
            ax.legend(['Total', 'Correct'], loc='upper left')
        # if i==0 or i==2:
        #     ax.set_ylabel('Count')
        if i==1 or i==3:
            ax.get_yaxis().set_visible(False)
        # if i==0 or i==1:
        #     ax.get_xaxis().set_visible(False)
        ax.set_title('Fig1.%d: '%(i+1)+description[i], fontdict={'fontsize': fsize_title})
        ax.set_ylim(0, 700)
        ax2 = ax.twinx()
        filtered_confidence = [str_confidence[j] for j in range(len(total)) if total[j] >= 10]
        filtered_acc_rate = [acc_rate[j] for j in range(len(total)) if total[j] >= 10]
        ax2.plot(filtered_confidence, filtered_acc_rate, color=col5, marker='o')
        # ax2.set_ylabel('Accuracy Rate (%)', color=col5)
        # ax2.set_ylim(20, max_acc_rate)
        ax2.set_ylim(10, 90)
        accuracy = sum(correct) / sum(total) * 100
        ax2.axhline(y=accuracy, color=col2, linestyle='--')
        ax2.text(6.6, accuracy, f'Overall Accuracy {accuracy:.2f}%', color=col1_, ha='right')

        if i==0 or i==2:
            ax2.get_yaxis().set_visible(False)

    # fig.tight_layout()
    # fig.subplots_adjust(hspace=0.5)
    # fig.suptitle('Confidence vs. Count and Accuracy Rate')
    fig.text(0.5, 0.04, 'Confidence(8 forward passes)', 
             ha='center', fontdict={'fontsize': fsize_text})
    fig.text(0.04, 0.5, 'Counts', va='center', rotation='vertical', 
             color=col1_, fontdict={'fontsize': fsize_text})
    fig.text(0.96, 0.5, 'Accuracy Rate (%)', va='center', rotation='vertical', 
             color=col5, fontdict={'fontsize': fsize_text})

    fig.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.1, hspace=0.22, wspace=0.1)

    # set picture size
    fig.set_dpi(500.0)
    # print(fig.get_dpi()) # 200.0
    fig.set_size_inches(12, 6)

    # plt.show()

    fig.savefig('report/Figures/plot_predictions_2x2.png')


if __name__ == '__main__':
    json_fpath = 'predictions/test_2411081717.jsonl'
    plot_predictions(json_fpath)

    json_fpath_list = ['predictions/test_241108.jsonl',
                       'predictions/test_2411081107.jsonl',
                       'predictions/test_2411081414.jsonl',
                       'predictions/test_2411082338.jsonl']
    plot_predictions_2x2(json_fpath_list)