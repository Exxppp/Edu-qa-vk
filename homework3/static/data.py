from builder import Builder


class DataBuilder:
    @staticmethod
    def data_auth(login, password):
        data = {
            'email': login,
            'password': password,
            'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
        }
        return data

    @staticmethod
    def data_create_company(name):
        company_data = Builder.company()
        data = {"name": name,
                "objective": "general_ttm",
                "price": company_data.price,
                "package_id": 451, "banners": [{"urls": {"primary": {"id": 697543}},
                                                "textblocks": {"title_25": {"text": company_data.title},
                                                               "text_90": {"text": company_data.text}},
                                                "content": {"image_90x75": {"id": 8700}}}]}
        return data

    @staticmethod
    def data_delete_company(id_company):
        data = [
            {"id": id_company, "status": "deleted"}
        ]
        return data

    @staticmethod
    def data_create_segment(name):
        data = {"name": name,
                "pass_condition": 1,
                "relations": [{"object_type": "remarketing_player",
                               "params": {"type": "positive",
                                          "left": 365,
                                          "right": 0}},
                              {"object_type": "remarketing_payer",
                               "params": {"type": "positive",
                                          "left": 365,
                                          "right": 0}}],
                "logicType": "or"}
        return data

    @staticmethod
    def data_create_source_vk_edu(id_vk_edu):
        data = {
            "items": [{"object_id": id_vk_edu}]
        }
        return data

    @staticmethod
    def data_create_segment_vk_edu(id_group, name):
        data = {
            "name": name,
            "pass_condition": 1,
            "relations": [{"object_type": "remarketing_vk_group",
                           "params": {"source_id": id_group,
                                      "type": "positive"}}],
            "logicType": "or"
        }
        return data
