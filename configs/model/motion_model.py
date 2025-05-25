import os
path = "D:\\PyCharmWorkSpace\\VH\\MuseV\\checkpoints\\motion"
MODEL_CFG = {
    "musev": {
        "unet": path+"\\"+ "musev",
        "desp": "only train unet motion module, fix t2i",
    },
    "musev_referencenet": {
        "unet": path+"\\"+"musev_referencenet",
        "desp": "train referencenet, IPAdapter and unet motion module, fix t2i",
    },
    "musev_referencenet_pose": {
        "unet": path+"\\"+"musev_referencenet_pose",
        "desp": "train  unet motion module and IPAdapter, fix t2i and referencenet",
    },
}
