from typing import Dict


class SystemAPIMixin:
    """API for accessing general system information of the camera."""
    def get_general_system(self) -> Dict:
        """:return: response json"""
        body = [{"cmd": "GetTime", "action": 1, "param": {}}, {"cmd": "GetNorm", "action": 1, "param": {}}]
        return self._execute_command('get_general_system', body, multi=True)

    def get_time_json(self) -> Dict:
        """:return: response json"""
        body = [{"cmd": "GetTime", "action": 1, "param": {}}]
        return self._execute_command('GetTime', body)[0]

    def set_time(self):
        # TODO:
        raise NotImplementedError("set_time() is not implemented yet")
    
    def update_time(self, year : int, month : int, day : int, hour : int, minute : int, second : int):
        # Input validation
        if type(year) is not int:
            raise ValueError("year must be an integer")
        
        if type(month) is not int or month < 1 or month > 12:
            raise ValueError("month must be an integer")
        
        if type(day) is not int or day < 1 or day > 31:
            raise ValueError("day must be an integer")
        
        if type(hour) is not int or hour < 0 or hour > 23:
            raise ValueError("hour must be an integer")
        
        if type(minute) is not int or minute < 0 or minute > 59:
            raise ValueError("minute must be an integer")
        
        if type(second) is not int or second < 0 or second > 59:
            raise ValueError("second must be an integer")
        
        current_settings = self.get_time_json()
        
        time_settings = {
            "year" : year,
            "mon" : month,
            "day" : day,
            "hour" : hour,
            "min" : minute,
            "sec" : second,
            "hourFmt" : current_settings["Time"]["hourFmt"],
            "timeFmt" : current_settings["Time"]["timeFmt"],
            "timeZone" : current_settings["Time"]["timeZone"]
        }
        
        command_parameters = {
            "Dst" : current_settings["Dst"],
            "Time": time_settings
        }
        
        body = [{"cmd": "SetTime", "action": 0, "param": command_parameters}]
        
        return self._execute_command('SetTime', body, multi=True)

    def get_performance(self) -> Dict:
        """
        Get a snapshot of the current performance of the camera.
        See examples/response/GetPerformance.json for example response data.
        :return: response json
        """
        body = [{"cmd": "GetPerformance", "action": 0, "param": {}}]
        return self._execute_command('GetPerformance', body)

    def get_information(self) -> Dict:
        """
        Get the camera information
        See examples/response/GetDevInfo.json for example response data.
        :return: response json
        """
        body = [{"cmd": "GetDevInfo", "action": 0, "param": {}}]
        return self._execute_command('GetDevInfo', body)

    def reboot_camera(self) -> Dict:
        """
        Reboots the camera
        :return: response json
        """
        body = [{"cmd": "Reboot", "action": 0, "param": {}}]
        return self._execute_command('Reboot', body)

    def get_dst(self) -> Dict:
        """
        Get the camera DST information
        See examples/response/GetDSTInfo.json for example response data.
        :return: response json
        """
        body = [{"cmd": "GetTime", "action": 0, "param": {}}]
        return self._execute_command('GetTime', body)
