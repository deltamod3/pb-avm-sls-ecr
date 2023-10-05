from collections import OrderedDict

import joblib
import numpy as np

model_dir = "./models"
RENT_MODEL_NAME = "lgbm_rent.joblib"
SALE_MODEL_NAME = "lgbm_sale.joblib"


def get_price(data: dict) -> float:
    if data["type"] == "sale":
        model = joblib.load(f"{model_dir}/{SALE_MODEL_NAME}")
    elif data["type"] == "rent":
        model = joblib.load(f"{model_dir}/{RENT_MODEL_NAME}")
    else:
        raise KeyError("Only `sale` or `rent` is supported")
    template = OrderedDict(
        {
            "features.propertyType": None,
            "features.beds": data.get("features.beds", 2.233 if data["type"] == "rent" else 3.171),
            "features.baths": data.get("features.baths", 1.288 if data["type"] == "rent" else 1.395),
            "lat": data["lat"],
            "lon": data["lon"],
            # "cluster": None,
        }
    )
    ord_encoder = joblib.load(f"{model_dir}/ord_encoder.joblib")
    template["features.propertyType"] = ord_encoder.transform(
        [[data["features.propertyType"]]]
    )

    # cluster = joblib.load(f"{model_dir}/cluster.joblib")
    # template["cluster"] = cluster.predict(
    #     np.array([[data["lat"], data["lon"]]], dtype=np.float32)
    # )
    return model.predict(np.array([list(template.values())], dtype=np.float32))[0]
