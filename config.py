

# parser.add_argument("-m", "--model", type=str, default="config/yolov3.cfg", help="Path to model definition file (.cfg)")
# parser.add_argument("-d", "--data", type=str, default="config/coco.data", help="Path to data config file (.data)")
# parser.add_argument("-e", "--epochs", type=int, default=300, help="Number of epochs")
# parser.add_argument("-v", "--verbose", action='store_true', help="Makes the training more verbose")
# parser.add_argument("--n_cpu", type=int, default=8, help="Number of cpu threads to use during batch generation")
# parser.add_argument("--pretrained_weights", type=str, help="Path to checkpoint file (.weights or .pth). Starts training from checkpoint model")
# parser.add_argument("--checkpoint_interval", type=int, default=1, help="Interval of epochs between saving model weights")
# parser.add_argument("--evaluation_interval", type=int, default=1, help="Interval of epochs between evaluations on validation set")
# parser.add_argument("--multiscale_training", action="store_true", help="Allow multi-scale training")
# parser.add_argument("--iou_thres", type=float, default=0.5, help="Evaluation: IOU threshold required to qualify as detected")
# parser.add_argument("--conf_thres", type=float, default=0.1, help="Evaluation: Object confidence threshold")
# parser.add_argument("--nms_thres", type=float, default=0.5, help="Evaluation: IOU threshold for non-maximum suppression")
# parser.add_argument("--logdir", type=str, default="logs", help="Directory for training log files (e.g. for TensorBoard)")
# parser.add_argument("--seed", type=int, default=-1, help="Makes results reproducable. Set -1 to disable.")

import os

class Config:
    data_dir  = "../data/Gaze_Data/"
    data_file = os.path.join(data_dir, "gaze.data")
    num_workers = 2
    verbose = True

    save_dir  = "runs/EXP1_GAZE"
    log_dir   = os.path.join(save_dir,"logs")
    ckpt_dir  = os.path.join(save_dir, "checkpoints")

    model_def          = os.path.join(data_dir, "model.cfg")
    pretrained_weights = ""

    epochs     = 300
    iou_thres  = 0.5
    conf_thres = 0.1
    nms_thres  = 0.5
    seed       = 100
    multiscale = False

    checkpoint_interval = 5
    evaluation_interval = 1

    




