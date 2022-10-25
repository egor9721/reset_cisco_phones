import paramiko
import csv
import config
import time


class Device(object):

    def __init__(self, host, model):
        self.host = host
        self.model = model
        self.login = None
        self.pwd = None
        self.command_for_reset_all = None
        self.command_for_reset_certs = None
        self.command_for_reboot = None
        self.port = None
        self.error = None

    def ssh_connect(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.host, username=config.LOGIN, password=config.PASSWORD, port=self.port)
            ssh = client.invoke_shell()
            return ssh
        except:
            print('Can not connection to deice.\n'
                  'Check availability to device and credentials in config file')
            self.error = 1

    def check_model(self):
        for model in config.MODELS:
            if model['model'] == self.model:
                self.login = model['login']
                self.pwd = model['pwd']
                self.command_for_reset_all = model['reset_all']
                self.command_for_reset_certs = model['reset_cert']
                self.port = model['port']
                return True

        print('device model not found')
        return False

    def reset_all(self):
        ssh = self.ssh_connect()
        if not self.error:
            if not self.login:
                print('this device have not login')
            else:
                ssh.send(f'{self.login}\n')
                time.sleep(1)
                ssh.send(f'{self.pwd}\n')
                time.sleep(1)
                if self.command_for_reset_all:
                    ssh.send(f'{self.command_for_reset_all}\n')
                    time.sleep(1)
                    print('Reset all complete')
                else:
                    print('Device have not command for reset device')
                ssh.close()

    def reset_itl(self):
        ssh = self.ssh_connect()
        if not self.error:
            if not self.login:
                print('This device have not login')
            else:
                ssh.send(f'{self.login}\n')
                time.sleep(1)
                ssh.send(f'{self.pwd}\n')
                time.sleep(1)
                if self.command_for_reset_certs:
                    ssh.send(f'{self.command_for_reset_certs}\n')
                    print('Reset certs complete')
                    time.sleep(1)
                else:
                    print('Device have not command for reset trust certs')
                ssh.close()

    def reboot(self):
        ssh = self.ssh_connect()
        if not self.error:
            if not self.login:
                print('this device have not login')
            else:
                ssh.send(f'{self.login}\n')
                time.sleep(1)
                ssh.send(f'{self.pwd}\n')
                time.sleep(1)
                if self.command_for_reboot:
                    ssh.send(f'{self.command_for_reboot}\n')
                    print('Reboot complete')
                    time.sleep(1)
                else:
                    print('device have not command for reboot')
                ssh.close()


def intro():
    print('this script for execute command on phone devices with ssh.\n'
          'You can execute command interactive or automaticaly.\n'
          'If you press "interactive", you should enter hostname device and device model.\n'
          'After that you choose command and this command will be execute.\n'
          'If you press "auto", you should enter path to file with devices.\n'
          'This file must contain hostname and device model.\n'
          'After that you choose command and this command will be execute.\n'
          '-------------------------------------------------------------------------------')


def main():
    intro()
    while True:
        mode = input('Enter type for works script:\n'
                                  '[1] Auto\t[2] Interactive\t [0] Exit\n')
        if mode == '1':
            filename = input('Enter to filepath: \n')
            devices = []
            with open(filename, 'r', encoding='utf-8') as f:
                data = csv.DictReader(f)
                for row in data:
                    devices.append(row)
            command = input('Enter command:\n'
                            '[1] Reset device\t [2] Reset trust certs\t [3] Reboot device\n')
            print('--------------------------------------------')
            for device in devices:
                print('\ndevice: {}'.format(device['Device Name']))
                ssh_device = Device(host=device['Device Name'], model=device['Model'])
                if ssh_device.check_model():
                    if command == '1':
                        ssh_device.reset_all()
                    elif command == '2':
                        ssh_device.reset_itl()
                    elif command == '3':
                        ssh_device.reboot()
                    else:
                        print('incorrect command')
                        break
                print('----------------------------------------')
        elif mode == '2':
            hostname = input('Enter hostname device:\n')
            model = input('Enter device model (example: Cisco 7811):\n')
            command = input('Enter command:\n'
                            '[1] Reset device\t [2] Reset trust certs\t [3] Reboot device\n')
            ssh_device = Device(host=hostname, model=model)
            if ssh_device.check_model():
                if command == '1':
                    ssh_device.reset_all()
                elif command == '2':
                    ssh_device.reset_itl()
                elif command == '3':
                    ssh_device.reboot()
            print('----------------------------------------')
        elif mode == '0':
            break
        else:
            print('incorrect command')


if __name__ == '__main__':
    main()
