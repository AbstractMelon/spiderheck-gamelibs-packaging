import os
import shutil
spiderheck = "/run/media/kyles/Storage/SteamLibrary/steamapps/common/SpiderHeck/SpiderHeckApp_Data/Managed"
assemblies = [
    "Accessibility",
    "Assembly-CSharp",
    "Assembly-CSharp-firstpass",
    "Cinemachine",
    "DDebug",
    "DoozyEngine",
    "DOTween",
    "DOTween.Modules",
    "EasySave3",
    "GdkUtilities",
    "I2",
    "JunTween",
    "Mono.Security",
    "MyScriptAssembly",
    "NewAssembly",
    "Pathfinding.Ionic.Zip.Reduced",
    "SteamP2P Transport for Netcode for GameObjects",
    "Steamworks.NET",
    "Unity.2D.Animation.Runtime",
    "Unity.2D.Common.Runtime",
    "Unity.Collections",
    "Unity.InputSystem",
    "Unity.Mathematics",
    "Unity.Netcode.Components",
    "Unity.Netcode.Runtime",
    "Unity.TextMeshPro",
    "Unity.Timeline",
    "UnityEngine.CoreModule",
    "UnityEngine.UI",
    "UnityEngine.ImageConversionModule",
    "UnityEngine.Physics2DModule",
    "UnityEngine.IMGUIModule"
]
if os.path.isdir("lib"):
    shutil.rmtree("lib")
os.mkdir("lib")
for assembly in assemblies:
    item_path = spiderheck + "/" + assembly + ".dll"
    item = assembly + ".dll"
    print(f"Processing: {item}")
    shutil.copyfile(item_path, "lib/" + item)
    os.system(f"assembly-publicizer \"lib/{item}\" --strip")
    os.remove(f"lib/{item}")
    print("Renaming file")
    os.rename(f"lib/{assembly}-publicized.dll", f"lib/{item}")
os.system("mono /usr/local/bin/nuget.exe pack SpiderHeck.GameLibs.nuspec")
