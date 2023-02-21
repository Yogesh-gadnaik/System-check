import platform
import psutil
import wmi

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]
# crete empty dictionary
sys_info = {}

# inserting all info in dictionary from both platform and psutil module
sys_info[1] = platform.system()
sys_info[2] = platform.node()
sys_info[3] = platform.release()
sys_info[4] = platform.version()
sys_info[5] = platform.machine()
sys_info[6] = platform.processor()
sys_info[7] = platform.architecture()
sys_info[8] = platform.platform()
sys_info[9] = psutil.virtual_memory()
sys_info[10] = psutil.cpu_count(logical=False)
sys_info[11] = psutil.cpu_count(logical=True)
sys_info[12] = psutil.cpu_freq().current
sys_info[13] = psutil.cpu_freq().min
sys_info[14] = psutil.cpu_freq().max
sys_info[15] = psutil.cpu_percent(interval=1)
sys_info[16] = psutil.cpu_percent(interval=1, percpu=True)
sys_info[17] = my_system.Manufacturer
sys_info[18] = my_system. Model
sys_info[19] = my_system.Name
sys_info[20] = my_system.NumberOfProcessors
sys_info[21] = my_system.SystemType
sys_info[22] = my_system.SystemFamily
list = ['exit', 'system', 'node', 'release', 'version', 'machine', 'processor', 'architecture_details', 'platform_details', 'virtual_memory', 'physical_core', 'logical_core',
        'cpu_frequency', 'min_frequency', 'max_frequency', 'cpu_utilization', 'per_cpu_utilization', 'manufacturer', 'model', 'sysname', 'no_processors', 'systemtype', 'systemfamily', 'allinfo']
# Asking user which info do you want to display
info = 20
while info != '0':
    info = int(input("WHICH SYSTEM INFORMATION DO YOU WANT?? \n 0.exit \n 1.system,\n 2.node,\n 3.release,\n 4.version,\n 5.machine,\n 6.processor,\n 7.architecture_details,\n 8.platform_details,\n 9.virtual_memory,\n 10.physical_core,\n 11.logical_core,\n 12.cpu_frequency,\n 13.min_frequency,\n 14.max_frequency,\n 15.cpu_utilization,\n 16.per_cpu_utilization,\n 17.manufacturer,\n 18.model,\n 19.sysname,\n 20.no_processors,\n 21.systemtype,\n 22.systemfamily,\n 23.allinfo --->"))
    print()
    try:
        if info == 0:
            break
        if info == 23:
            print("Your output for", list[info], "is :")
            for i, j in sys_info.items():
                print(list[i], " - ", j)
            print("-"*100)
        else:
            print("Your output for", list[info], "is :")
            print(list[info], ':', sys_info[info])
            print("-"*100)

    except Exception as e:
        print(e)
        print("Please,Enter proper system information as shown in above list")
        print("-"*100)
