import subprocess

EXTRAS = {
    "badpackets": "ftdbN0KK",
    "Better Beds": "kKwy3HU9",
    "Better Mount Hud": "kqJFAPU9",
    "Better F3": "8shC1gFX",
    "Blur (Fabric)": "NK39zBp2",
    "Continuity": "1IjD5062",
    "Debugify": "QwxR6Gcd",
    "Dynamic FPS": "LQ3K71Q1",
    "Enhanced Block Entities": "OVuFYfre",
    "Fabric Language Kotlin": "Ha28R6CL",
    "Falling Leaves": "WhbRG4iK",
    "FastAnim": "yHf7SALy",
    "immediatelyFast": "5ZwdcRci",
    "Memory Leak Fix": "NRjRiSSD",
    "More Culling": "51shyZVL",
    "Mouse Tweaks": "aC3cM3Vq",
    "Reese's Sodium Options": "Bh37bMuy",
    "ShulkerBoxTooltip": "2M01OLQq",
    "Sodium Extras": "PtjYWJkn",
    "Visuality": "rI0hvYcd",
    "WTHIT": "6AQIaxuO",
    "YetAnotherConfigLib": "1eAoo2KR",
}

for (mod, id) in EXTRAS.items():
    print(f"Adding {mod}")
    subprocess.run(["./packwiz", "mr", "add", id])

