EXPECTED_DIFF_DICT = {
    'common': {
        'type_of_change': 'intact',
        'key_type': 'nested_key',
        'value': {
            'follow': {
                'type_of_change': 'added',
                'key_type': 'flat_key',
                'value': False  
            },
            'setting1': {
                'type_of_change': 'intact',
                'key_type': 'flat_key',
                'value': 'Value 1' 
            },
            'setting2': {
                'type_of_change': 'deleted',
                'key_type': 'flat_key',
                'value': 200  
            },
            'setting3': {
                'type_of_change': 'updated',
                'old_value': True, 
                'new_value': None,  
                'old_key_type': 'flat_key', 
                'new_key_type': 'flat_key'   
            },
            'setting4': {
                'type_of_change': 'added',
                'key_type': 'flat_key',
                'value': 'blah blah'  
            },
            'setting5': {
                'type_of_change': 'added',
                'key_type': 'nested_key',
                'value': {
                    'key5': {
                        'type_of_change': 'intact',
                        'key_type': 'flat_key',
                        'value': 'value5'  
                    }
                }
            },
            'setting6': {
                'type_of_change': 'intact',
                'key_type': 'nested_key',
                'value': {
                    'doge': {
                        'type_of_change': 'intact',
                        'key_type': 'nested_key',
                        'value': {
                            'wow': {
                                'type_of_change': 'updated',
                                'old_value': '',  
                                'new_value': 'so much',
                                'old_key_type': 'flat_key',
                                'new_key_type': 'flat_key'
                            }
                        }
                    },
                    'key': {
                        'type_of_change': 'intact',
                        'key_type': 'flat_key',
                        'value': 'value'  
                    },
                    'ops': {
                        'type_of_change': 'added',
                        'key_type': 'flat_key',
                        'value': 'vops'  
                    }
                }
            }
        }
    },
    'group1': {
        'type_of_change': 'intact',
        'key_type': 'nested_key',
        'value': {
            'baz': {
                'type_of_change': 'updated',
                'old_value': 'bas', 
                'new_value': 'bars', 
                'old_key_type': 'flat_key',
                'new_key_type': 'flat_key'
            },
            'foo': {
                'type_of_change': 'intact',
                'key_type': 'flat_key',
                'value': 'bar' 
            },
            'nest': {
                'type_of_change': 'updated',
                'old_value': {
                    'key': {
                        'type_of_change': 'intact',
                        'key_type': 'flat_key',
                        'value': 'value'  
                    }
                },
                'new_value': 'str',  
                'old_key_type': 'nested_key',  
                'new_key_type': 'flat_key'      
            }
        }
    },
    'group2': {
        'type_of_change': 'deleted',
        'key_type': 'nested_key',
        'value': {
            'abc': {
                'type_of_change': 'intact',
                'key_type': 'flat_key',
                'value': 12345 
            },
            'deep': {
                'type_of_change': 'intact',
                'key_type': 'nested_key',
                'value': {
                    'id': {
                        'type_of_change': 'intact',
                        'key_type': 'flat_key',
                        'value': 45  
                    }
                }
            }
        }
    },
    'group3': {
        'type_of_change': 'added',
        'key_type': 'nested_key',
        'value': {
            'deep': {
                'type_of_change': 'intact',
                'key_type': 'nested_key',
                'value': {
                    'id': {
                        'type_of_change': 'intact',
                        'key_type': 'nested_key',
                        'value': {
                            'number': {
                                'type_of_change': 'intact',
                                'key_type': 'flat_key',
                                'value': 45  
                            }
                        }
                    }
                }
            },
            'fee': {
                'type_of_change': 'intact',
                'key_type': 'flat_key',
                'value': 100500  
            }
        }
    }
}