#
# Copyright © 2018, "rupansh" <rupanshsekar@hotmail.com>
#
# This software is licensed under the terms of the GNU General Public
# License version 2, as published by the Free Software Foundation, and
# may be copied, distributed, and modified under those terms.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# Please maintain this if you use this script or any part of it

from git import *
import os

logo = str(""" ______   ______     ______     ______        ______     __         ______     __   __     ______     ______   
/\__  _\ /\  == \   /\  ___\   /\  ___\      /\  ___\   /\ \       /\  __ \   /\ "-.\ \   /\  ___\   /\  == \  
\/_/\ \/ \ \  __<   \ \  __\   \ \  __\      \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-.  \  \ \  __\   \ \  __<  
   \ \_\  \ \_\ \_\  \ \_____\  \ \_____\     \ \_____\  \ \_____\  \ \_____\  \ \_\\\\"\_\  \ \_____\  \ \_\ \\ \\
    \/_/   \/_/ /_/   \/_____/   \/_____/      \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_____/   \/_/ /_/
Note- This script is only for Redmi 3s(ie. land)
Tip- Run this from your ROM's source dir if you are cloning dt,kernel and vendor
~Brought to you by RUPANSHKEK
~GPL V2
~Made with love""")
print(logo)


def tree(link, directory, br):
    if os.path.isdir(directory):
        print(directory+" exists! It won't be cloned!")
    else:
        repo = Repo.clone_from(
            link, directory,
            branch=br
        )
        print(directory+" Tree Cloned!")


device = "device/xiaomi/land"
vendor = "vendor/xiaomi"
kernel = "kernel/xiaomi/msm8937"
common = "device/xiaomi/msm8937-common"

c_dir = "chimera"
dtc_dir = "dtc-8.0"
ak2_dir = "AnyKernel2"
linaro_dir = "aarch64-linux-gnu"

bc = "lineage-16.0"
dc = "dtc-8.0-140918"
ak2br = "land"
linbr = "linaro-7-14092018"

chimera = "https://github.com/ChimeraKernelProject/chimera_land-current"
dtc_8 = "https://github.com/ChimeraKernelProject/dragontc-8.0"
ak2 = "https://github.com/ChimeraKernelProject/AnyKernel2"
linaro = "https://bitbucket.org/rupanshji/aarch64-linux-gnu.git"

chimera = [(chimera, c_dir, bc), (dtc_8, dtc_dir, dc), (ak2, ak2_dir, ak2br), (linaro, linaro_dir, linbr)]
devices = [1, device, 3]
vendors = [1, vendor, 3]
kernels = [1, kernel, 3]
trees = [devices, vendors, kernels]

ask = input("What are you cloning today?(trees/chimera) ")
if ask == "trees":
    ask2 = input("Whose trees do you want to clone?(ritesh/hyper) ")
    if ask2 == "ritesh":
        print("Note:- RiteshSaxena's Trees are treble")
        devices[0] = "https://github.com/RiteshSaxena/android_device_xiaomi_land"
        vendors[0] = "https://github.com/RiteshSaxena/proprietary_vendor_xiaomi"
        kernels[0] = "https://github.com/RiteshSaxena/android_kernel_xiaomi_msm8937"
        verask = input("Which Android version?(O/P) ")
        if verask == "O":
            devices[2] = "lineage-15.1"
            vendors[2] = "lineage-15.1-land"
            kernels[2] = "lineage-15.1"
        elif verask == "P":
            devices[2] = "lineage-16.0"
            vendors[2] = "lineage-16.0-land"
            kernels[2] = "lineage-16.0"
        else:
            print("Incorrect Android Version! Enter O or P")
        for i in trees:
            tree(*i)
        print("RiteshSaxena's {} Trees Cloned".format(verask))

    elif ask2 == "hyper":
        devices[0] = "https://github.com/HyperTeam/android_device_xiaomi_land"
        t_common = "https://github.com/HyperTeam/android_kernel_xiaomi_msm8937"
        vendors[0] = "https://github.com/HyperTeam/proprietary_vendor_xiaomi.git"
        kernels[0] = "https://github.com/HyperTeam/android_kernel_xiaomi_msm8937"
        ask3 = input("Which android version?(N/O) ")
        if ask3 == "N":
            devices[2] = "cm-14.1"
            vendors[2] = devices[2]
            kernels[2] = devices[2]
            trees.append((t_common, common, devices[2]))
        elif ask3 == "O":
            devices[2] = "lineage-15.1"
            vendors[2] = devices[2]
            kernels[2] = devices[2]
            trees.append((t_common, common, devices[2]))
        else:
            print("Wrong input! Please enter the correct version")
        for i in trees:
            tree(*i)
        print("HyperTeam {} trees cloned".format(ask3))
        os.system("rm -rf vendor/xiaomi/santoni")

    else:
        print("Wrong input! Enter the correct team name!")

elif ask == "chimera":
    c_ask = input("Are we cloning the required tools?(ie. Toolchains, Anykernel2) y/n ")
    if c_ask == "y":
        for i in chimera:
            tree(*i)
        print("Chimera Kernel Cloned with The Required tools")
    elif c_ask == "n":
        tree(*chimera[0])
        print("Chimera Kernel Cloned without the required tools")
    else:
        print("Incorrect input! Enter y or n only!")

else:
    print("Wrong input! Enter what you want to clone correctly!")
