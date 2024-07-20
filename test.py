# from CattleScanner import predict
# side_img = "/Users/aftaabhussain/Work/Data Accumulator and prediction/Images/Side/127_b4-1_s_131_M.jpg"
# rear_img = "/Users/aftaabhussain/Work/Data Accumulator and prediction/Images/Rear/127_b4-1_r_131_M.jpg"
#
# weight = predict(side_img, rear_img)
# print(f"The weight is {weight} kg")

# from CattleScanner import predict
from CattleScanner.Cattle_inference import CattleWeight
import CattleScanner
import os


path = os.path.dirname(CattleScanner.__file__)
model = CattleWeight(cwd = path)
side_img = "/Users/aftaabhussain/Work/Data Accumulator and prediction/Images/Side/127_b4-1_s_131_M.jpg"
rear_img = "/Users/aftaabhussain/Work/Data Accumulator and prediction/Images/Rear/127_b4-1_r_131_M.jpg"

weight = model.predict(side_img, rear_img)
print(f"The weight is {weight} kg")
