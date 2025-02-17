# T-YOLO: A Novel Detection Model for Small Target 
Abstract：Tiny-scale and high-density in target detection research field are the main challenges. Traditional detection
methods have problems of imprecise key feature representation and low recognition accuracy on small targets.
To circumvent this problem, an specialized small target detection model (T-YOLO) is proposed. Initially, a 
slice-based auxiliary training strategy was raised to improve the capability of small target detection.
Furthermore, YOLOv8 network architecture was optimized by adding several object detection layers and widening 
the convolution width in the lower layers of Backbone. Finally, the adaptive CIoU-NWD was proposed by calculating
the Intersection over Union(IoU) between predicted and ground truth. To comprehensively evaluate the performance
of T-YOLO, the public datasets—VisDrone and AI-TOD was used to conduct this experiment. Experiment results 
demonstrate T-YOLO can achieve a maximum improvement of 9.6% and 14.8% of mAP0.5 on VisDrone and AI-TOD correspondingly.
This result demonstrates the proposed T-YOLO algorithm can effectively deal with actual potential application problems.

