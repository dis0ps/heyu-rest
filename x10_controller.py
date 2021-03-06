import subprocess


class x10_controller:

    def __init__(self, heyu_path):
        self.heyu_bin = heyu_path

    def __run_heyu(self, command_arguments):

        return_value = "Success"
        command_line = [self.heyu_bin]
        command_line.extend(command_arguments)

        try:
            results = subprocess.check_call(command_line)
        except:
            return_value = "Failed"

        return return_value

    def turn_on(self, house_code, device_number):
        target_command = ["on", house_code + device_number]
        results = self.__run_heyu(target_command)
        return results

    def turn_off(self, house_code, device_number):
        target_command = ["off", house_code + device_number]
        results = self.__run_heyu(target_command)
        return results

    def all_off(self, house_code):
        target_command = ["alloff", house_code]
        results = self.__run_heyu(target_command)
        return results
