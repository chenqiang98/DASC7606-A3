if [ -d 3036370891 ]
then
    rm -rf 3036370891
    mkdir 3036370891
else
    mkdir 3036370891
fi

mkdir 3036370891/src

cp report/7606A3.pdf 3036370891/7606A3_3036370891.pdf
cp report/README.md 3036370891/README.md
cp mcqa.py 3036370891/src/mcqa.py
cp modeling_llama.py 3036370891/src/modelling_llama.py
cp tokenization_llama_fast.py 3036370891/src/tokenization_llama_fast.py
cp configuration_llama.py 3036370891/src/configuration_llama.py
cp ./scripts/get_accuracy.py 3036370891/src/get_accuracy.py
cp -r ./predictions 3036370891/predictions

cd 3036370891
ln -s predictions/test_2411082338.jsonl model_predictions_66.64%.jsonl

cd ..
zip -r 3036370891.zip 3036370891 -x "*.DS_Store" -x "__MACOSX"