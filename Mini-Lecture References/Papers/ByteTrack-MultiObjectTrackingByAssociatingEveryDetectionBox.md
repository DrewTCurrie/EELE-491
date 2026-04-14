# Multi-Object Tracking (MOT) 

- Key ideas:
    - Instead of rejecting boxes that have low confidence thresholds, keep those fragments and attempt to sitch them together
    - By allowing for these fragements or "tracklets" to be logged a model can be trained that can better detect partially hidden objects in a video feed
    - This process allows for video tracking to be done even when frames are changing or when object are partially obstructed for frames

- Tracklets:
    - Low confidence detection boxes around objects
    - These are kept to keep objects detected over multiple frames, achieved through a Kalman to predict where the box must move for the next frame
    - Tracklets are not always shown on the final overaly but are kept internal when the confidence is below a set threshold to help avoid false positives


- Results
    - Against the HiEve benchmark (Humans in Events) ByteTrack ranks 1st among all leaderboards of HiEve. 
    - This is a robust tracking for humans in a crowded environment being able to get indiviuals out of a crowd
    