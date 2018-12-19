GENERAL_SCHEME = [
    {
        "field_name": "first_name",
        "field_type": "CharField",
        "kwargs": {
            "max_length": 50,
        }
    },
    {
        "field_name": "last_name",
        "field_type": "CharField",
        "kwargs": {
            "max_length": 50,
        }
    },
    {
        "field_name": "age",
        "field_type": "IntegerField",
        "kwargs": {
            "required": False,
        }
    },
    {
        "field_name": "subscribed",
        "field_type": "BooleanField",
        "kwargs": {
            "required": False,
            "initial": True,
        }
    },
]
