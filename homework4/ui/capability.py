def capability_select(device_os, file_path_to_app):
    if device_os == 'android':
        capability = {"platformName": "Android",
                      "platformVersion": "11.0",
                      "automationName": "Appium",
                      "appPackage": "ru.mail.search.electroscope",
                      "appActivity": ".ui.activity.AssistantActivity",
                      "app": file_path_to_app,
                      "orientation": "PORTRAIT"
                      }
    else:
        raise ValueError("Incorrect device os type")

    return capability
