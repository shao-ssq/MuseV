import os

IPAdapterModelDir = "D:\\PyCharmWorkSpace\\VH\\MuseV\\checkpoints\\IP-Adapter"

MotionDir = "D:\\PyCharmWorkSpace\\VH\\MuseV\\checkpoints\\motion"

MODEL_CFG = {
    "IPAdapter": {
        "ip_image_encoder": IPAdapterModelDir + "\\" + "image_encoder",
        "ip_ckpt": IPAdapterModelDir+ "\\" +  "ip-adapter-plus_sd15.bin",
        "ip_scale": 1.0,
        "clip_extra_context_tokens": 4,
        "clip_embeddings_dim": 1024,
        "desp": "",
    },
    "IPAdapterPlus": {
        "ip_image_encoder": IPAdapterModelDir + "\\" + "image_encoder",
        "ip_ckpt": IPAdapterModelDir+ "\\" +  "ip-adapter-plus_sd15.bin",
        "ip_scale": 1.0,
        "clip_extra_context_tokens": 16,
        "clip_embeddings_dim": 1024,
        "desp": "",
    },
    "IPAdapterPlus-face": {
        "ip_image_encoder": IPAdapterModelDir + "\\" + "image_encoder",
        "ip_ckpt":  IPAdapterModelDir + "\\" + "ip-adapter-plus-face_sd15.bin",
        "ip_scale": 1.0,
        "clip_extra_context_tokens": 16,
        "clip_embeddings_dim": 1024,
        "desp": "",
    },
    "IPAdapterFaceID": {
        "ip_image_encoder": IPAdapterModelDir + "\\" + "image_encoder",
        "ip_ckpt":  IPAdapterModelDir + "\\" +"ip-adapter-faceid_sd15.bin",
        "ip_scale": 1.0,
        "clip_extra_context_tokens": 4,
        "clip_embeddings_dim": 512,
        "desp": "",
    },
    "musev_referencenet": {
        "ip_image_encoder": IPAdapterModelDir + "\\" + "image_encoder",
        "ip_ckpt": MotionDir + "\\" + "musev_referencenet\\ip_adapter_image_proj.bin",
        "ip_scale": 1.0,
        "clip_extra_context_tokens": 4,
        "clip_embeddings_dim": 1024,
        "desp": "",
    },
    "musev_referencenet_pose": {
        "ip_image_encoder": IPAdapterModelDir + "\\" + "image_encoder",
        "ip_ckpt": MotionDir + "\\" + "musev_referencenet_pose/ip_adapter_image_proj.bin",
        "ip_scale": 1.0,
        "clip_extra_context_tokens": 4,
        "clip_embeddings_dim": 1024,
        "desp": "",
    },
}
