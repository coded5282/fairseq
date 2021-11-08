#!/bin/bash


python scripts/video_feature_extractor/extract.py \
    --vdir data/open-surgery-yt/videos \
    --fdir data/open-surgery-yt/feat/feat_how2_s3d \
    --type=s3d --num_decoding_thread=0 \
    --batch_size 32 --half_precision 1
