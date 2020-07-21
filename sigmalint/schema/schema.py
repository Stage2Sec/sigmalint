rx_schema = {
    "type": "//rec",
    "required": {
        "title": {
            "type": "//str",
            "length": {
                "min": 1,
                "max": 256
            }
        },
        "logsource": {
            "type": "//rec",
            "optional": {
                "category": "//str",
                "product": "//str",
                "service": "//str",
                "definition": "//str"
            }
        },
        "detection": {
            "type": "//rec",
            "required": {
                "condition": {
                    "type": "//any",
                    "of": [
                     {
                         "type": "//str"
                     },
                        {
                         "type": "//arr",
                         "contents": "//str",
                         "length": {
                             "min": 2
                         }
                     }
                    ]
                }
            },
            "optional": {
                "timeframe": "//str"
            },
            "rest": {
                "type": "//any",
                "of": [
                    {
                        "type": "//arr",
                        "contents": "//str"
                    },
                    {
                        "type": "//map",
                        "values": {
                            "type": "//any",
                            "of": [
                                {
                                    "type": "//str"
                                },
                                {
                                    "type": "//arr",
                                    "contents": "//str",
                                    "length": {
                                        "min": 2
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    },
    "optional": {
        "status": {
            "type": "//any",
            "of": [
                {
                    "type": "//str",
                    "value": "stable"
                },
                {
                    "type": "//str",
                    "value": "testing"
                },
                {
                    "type": "//str",
                    "value": "experimental"
                }
            ]
        },
        "description": "//str",
        "author": "//str",
        "references": {
            "type": "//arr",
            "contents": "//str"
        },
        "fields": {
            "type": "//arr",
            "contents": "//str"
        },
        "falsepositives": {
            "type": "//any",
            "of": [
                {
                    "type": "//str"
                },
                {
                    "type": "//arr",
                    "contents": "//str",
                    "length": {
                        "min": 2
                    }
                }
            ]
        },
        "level": {
            "type": "//any",
            "of": [
                {
                    "type": "//str",
                    "value": "low"
                },
                {
                    "type": "//str",
                    "value": "medium"
                },
                {
                    "type": "//str",
                    "value": "high"
                },
                {
                    "type": "//str",
                    "value": "critical"
                }
            ]
        }
    },
    "rest": "//any"
}

json_schema = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "minLength": 1,
            "maxLength": 256
        },
        "logsource": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string"
                },
                "product": {
                    "type": "string"
                },
                "service": {
                    "type": "string"
                },
                "definition": {
                    "type": "string"
                },
            },
            "anyOf": [
                {
                    "required": ["category"]
                },
                {
                    "required": ["product"]
                },
                {
                    "required": ["service"]
                }
            ],
            "additionalProperties": False
        },
        "detection": {
            "type": "object",
            "properties": {
                "condition": {
                    "anyOf": [
                        {
                            "type": "string"
                        },
                        {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "minItems": 2
                        }
                    ]
                },
                "timeframe": {
                    "type": "string"
                }
            },
            "additionalProperties": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    {
                        "type": "object",
                        "additionalProperties": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    },
                                    "minItems": 2
                                }
                            ]
                        }
                    }
                ]
            },
            "required": ["condition"]
        },
        "status": {
            "type": "string",
            "enum": ["stable", "testing", "experimental"]
        },
        "description": {
            "type": "string"
        },
        "references": {
            "type": "array",
            "items": {
                "type": {
                    "string"
                }
            }
        },
        "fields": {
            "type": "array",
            "items": {
                "type": {
                    "string"
                }
            }
        },
        "falsepositives": {
            "anyOf": [
                {
                    "type": "string"
                },
                {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "minItems": 2
                }
            ]
        },
        "level": {
            "type": "string",
            "enum": ["low", "medium", "high", "critical"]
        }
    },
    "required": ["title", "logsource", "detection"]
}

s2_schema = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "minLength": 1,
            "maxLength": 256
        },
        "logsource": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string"
                },
                "product": {
                    "type": "string"
                },
                "service": {
                    "type": "string"
                },
                "definition": {
                    "type": "string"
                },
            },
            "anyOf": [
                {
                    "required": ["category"]
                },
                {
                    "required": ["product"]
                },
                {
                    "required": ["service"]
                }
            ],
            "additionalProperties": False
        },
        "detection": {
            "type": "object",
            "properties": {
                "condition": {
                    "anyOf": [
                        {
                            "type": "string"
                        },
                        {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "minItems": 2
                        }
                    ]
                },
                "timeframe": {
                    "type": "string"
                }
            },
            "additionalProperties": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "object",
                                    "additionalProperties": {
                                        "anyOf": [
                                            {
                                                "type": ["string", "number"]
                                            },
                                            {
                                                "type": "array",
                                                "items": {
                                                    "type": ["string", "number"]
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "type": "object",
                        "additionalProperties": {
                            "anyOf": [
                                {
                                    "type": ["string", "number", "null"]
                                },
                                {
                                    "type": "array",
                                    "items": {
                                        "type": ["string", "number"]
                                    },
                                    "minItems": 1
                                }
                            ]
                        }
                    }
                ]
            },
            "required": ["condition"]
        },
        "status": {
            "type": "string",
            "enum": ["stable", "testing", "experimental"]
        },
        "description": {
            "type": "string"
        },
        "references": {
            "type": "array",
            "items": {
                "type": {
                    "string"
                }
            }
        },
        "fields": {
            "type": "array",
            "items": {
                "type": {
                    "string"
                }
            }
        },
        "falsepositives": {
            "anyOf": [
                {
                    "type": "string"
                },
                {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "minItems": 1
                }
            ]
        },
        "level": {
            "type": "string",
            "enum": ["low", "medium", "high", "critical"]
        }
    },
    "required": ["title", "logsource", "detection"]
}