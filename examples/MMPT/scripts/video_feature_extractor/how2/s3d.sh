#!/bin/bash


python scripts/video_feature_extractor/extract.py \
    --vdir data/videos \
    --fdir data/feat/feat_how2_s3d \
    --type=s3d --num_decoding_thread=0 \
    --batch_size 32 --half_precision 1
