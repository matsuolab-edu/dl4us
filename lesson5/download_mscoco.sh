# Train & validation captions
wget http://images.cocodataset.org/annotations/annotations_trainval2014.zip -P download/
unzip download/annotations_trainval2014.zip -d download/
rm ./download/annotations_trainval2014.zip

# Train images
wget http://images.cocodataset.org/zips/train2014.zip -P ./download/
unzip download/train2014.zip -d download/
rm ./download/train2014.zip

# Validation images
wget http://images.cocodataset.org/zips/val2014.zip -P download/
unzip download/val2014.zip -d download/
rm ./download/val2014.zip