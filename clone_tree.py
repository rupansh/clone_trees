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

logo = """ ______   ______     ______     ______        ______     __         ______     __   __     ______     ______   
/\__  _\ /\  == \   /\  ___\   /\  ___\      /\  ___\   /\ \       /\  __ \   /\ "-.\ \   /\  ___\   /\  == \  
\/_/\ \/ \ \  __<   \ \  __\   \ \  __\      \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-.  \  \ \  __\   \ \  __<  
   \ \_\  \ \_\ \_\  \ \_____\  \ \_____\     \ \_____\  \ \_____\  \ \_____\  \ \_\\"\_\  \ \_____\  \ \_\ \_\
    \/_/   \/_/ /_/   \/_____/   \/_____/      \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_____/   \/_/ /_/
Note- This script is only for Redmi 3s(ie. land)
Tip- Run this from your ROM's source dir if you are cloning dt,kernel and vendor
~Brought to you by RUPANSHKEK
~GPL V2
~Made with love"""
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

c_dir = "chimera_nich"
ct_dir = "chimera_treble"
dtc_dir = "dragontc-7.0"
ak2_dir = "AnyKernel2"
utc_dir = "aarch64-linux-android-4.9-kernel"

bc = "lineage-15.1"
dc = "master"
ak2br = "land"

chimera_nich = "https://github.com/rupansh/chimera_nich"
chimera_treble = "https://github.com/rupansh/chimera_treble"
dtc_7 = "https://github.com/USA-RedDragon/prebuilts_clang_host_linux-x86_7.0-DragonTC"
ak2 = "https://github.com/rupansh/AnyKernel2"
ubertc = "https://bitbucket.org/UBERTC/aarch64-linux-android-4.9-kernel.git"

chimera = [(chimera_nich, c_dir, bc), (chimera_treble, ct_dir, bc), (dtc_7, dtc_dir, dc), (ak2, ak2_dir, ak2br), (ubertc, utc_dir, dc)]

ask = input("What are you cloning today?(trees/chimera) ")
if ask == "trees":
    ask2 = input("Whose trees do you want to clone?(reloaded/hyper) ")
    if ask2 == "reloaded":
        print("Note:- TeamReloaded Trees are treble and only oreo trees are available!")
        t_device = "https://github.com/TeamReloaded/android_device_xiaomi_land"
        t_vendor = "https://github.com/TeamReloaded/proprietary_vendor_xiaomi"
        t_kernel = "https://github.com/TeamReloaded/android_kernel_xiaomi_msm8937"
        b = "lineage-15.1"
        bv = "lineage-15.1-land"
        trees = [(t_device, device, b), (t_vendor, vendor, bv), (t_kernel, kernel, b)]
        for i in trees:
            tree(*i)
        print("TeamReloaded trees cloned!")

    elif ask2 == "hyper":
        t_device = "https://github.com/HyperTeam/android_device_xiaomi_land"
        t_common = "https://github.com/HyperTeam/android_kernel_xiaomi_msm8937"
        t_vendor = "https://github.com/HyperTeam/proprietary_vendor_xiaomi.git"
        t_kernel = "https://github.com/HyperTeam/android_kernel_xiaomi_msm8937"
        ask3 = input("Which android version?(N/O) ")
        if ask3 == "N":
            b = "cm-14.1"
            trees = [(t_device, device, b), (t_vendor, vendor, b), (t_kernel, kernel, b), (t_common, common, b)]
            for i in trees:
                tree(*i)
            print("HyperTeam N trees cloned")
            os.system("rm -rf vendor/xiaomi/santoni")
        if ask3 == "O":
            b = "lineage-15.1"
            trees = [(t_device, device, b), (t_vendor, vendor, b), (t_kernel, kernel, b), (t_common, common, b)]
            for i in trees:
                tree(*i)
            print("HyperTeam O trees cloned")
            os.system("rm -rf vendor/xiaomi/santoni")
        else:
            print("Wrong input! Please enter the correct version")

    else:
        print("Wrong input! Enter the correct team name!")

elif ask == "chimera":
    c_ask = input("Which source are we cloning?(treble/normal/both) ")
    c_ask2 = input("Are we cloning the required repos?(ie. Toolchains, Anykernel2) y/n ")
    if c_ask == "treble":
        if c_ask2 == "y":
            del chimera[0]
            for i in chimera:
                tree(*i)
            print("Treble source cloned with ak2 and toolchains")
        elif c_ask2 == "n":
            tree(*chimera[1])
            print("Treble source cloned without ak2 and toolchains")
        else:
            print("Wrong input! Enter it correctly!")

    elif c_ask == "normal":
        if c_ask2 == "y":
            del chimera[1]
            for i in chimera:
                tree(*i)
            print("Non-treble source cloned with ak2 and toolchains")
        elif c_ask2 == "n":
            tree(*chimera[0])
            print("non-treble source cloned without ak2 and toolchains")
        else:
            print("Wrong input! Enter it correctly!")

    elif c_ask == "both":
        if c_ask2 == "y":
            for i in chimera:
                tree(*i)
            print("both sources cloned with ak2 and toolchains")
        elif c_ask2 == "n":
            tree(*chimera[0])
            tree(*chimera[1])
            print("both sources cloned without ak2 and toolchains")
        else:
            print("Wrong input! Enter it correctly!")

    else:
        print("Wrong Input ! enter the source name correctly!")

else:
    print("Wrong input! Enter what you want to clone correctly!")
