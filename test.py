import os

import CattleScanner
from CattleScanner.Cattle_inference import CattleRumination
from CattleScanner.Cattle_inference import CattleWeight

path = os.path.dirname(CattleScanner.__file__)

############################## Weight inference ############################
weight_model = CattleWeight(cwd=path)
side_img = "/Users/aftaabhussain/Work/Data Accumulator and prediction/Images/Side/127_b4-1_s_131_M.jpg"
rear_img = "/Users/aftaabhussain/Work/Data Accumulator and prediction/Images/Rear/127_b4-1_r_131_M.jpg"

weight = weight_model.predict(side_img, rear_img)
print(f"The weight is {weight} kg")

############################## rumination inference ############################
input_video_path1 = "samples/rumination.mp4"
input_video_path2 = "samples/rumination2.mp4"

output_dir = "outputs"

rumination_model = CattleRumination(cwd=path)
rumination = rumination_model.run_video_inference(input_video_path2, output_dir)
print(f'Rumination is {rumination} per minute')
