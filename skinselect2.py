import tkinter as tk
from tkinter import ttk
import os
import json

# Dictionary of available skins for each weapon
available_skins = {
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_G3.BP_Firearm_G3_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_G3A3_Hunter.BP_UG_Skin_G3A3_Hunter_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_G3A3_NocturneBlue.BP_UG_Skin_G3A3_NocturneBlue_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_G3A3_TwitchGreen.BP_UG_Skin_G3A3_TwitchGreen_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_PF940.BP_Firearm_PF940_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_PF940_NocturneBlue.BP_UG_Skin_PF940_NocturneBlue_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_PF940_TwoTone.BP_UG_Skin_PF940_TwoTone_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_PF940_TwitchGreen.BP_UG_Skin_PF940_TwitchGreen_C"
     ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_MDR.BP_Firearm_MDR_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MDR_Veteran.BP_UG_Skin_MDR_Veteran_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_MK18.BP_Firearm_MK18_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MK18_Veteran.BP_UG_Skin_MK18_Veteran_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MK18_DesertHex.BP_UG_Skin_MK18_DesertHex_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_M4A1.BP_Firearm_M4A1_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M4A1_NocturneBlue.BP_UG_Skin_M4A1_NocturneBlue_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M4A1_Camo.BP_UG_Skin_M4A1_Camo_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M4A1_TwoTone.BP_UG_Skin_M4A1_TwoTone_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M4A1_TwitchGreen.BP_UG_Skin_M4A1_TwitchGreen_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M4A1_UniversalDigital.BP_UG_Skin_M4A1_UniversalDigital_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_AK74.BP_Firearm_AK74_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AK74_Whiteout.BP_UG_Skin_AK74_Whiteout_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AK74_UrbanDigital.BP_UG_Skin_AK74_UrbanDigital_C",
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_G3.BP_Firearm_G3_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_G3A3_Hunter.BP_UG_Skin_G3A3_Hunter_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_G3A3_NocturneBlue.BP_UG_Skin_G3A3_NocturneBlue_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_G3A3_TwitchGreen.BP_UG_Skin_G3A3_TwitchGreen_C",
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_Fal.BP_Firearm_Fal_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_FAL_Chrome.BP_UG_Skin_FAL_Chrome_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_FAL_Damascus.BP_UG_Skin_FAL_Damascus_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_FAL_RedDark.BP_UG_Skin_FAL_RedDark_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_FAL_Whiteout.BP_UG_Skin_FAL_Whiteout_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_FAL_WoodBurn.BP_UG_Skin_FAL_WoodBurn_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_AUG.BP_Firearm_AUG_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AUG_BlackPowder.BP_UG_Skin_AUG_BlackPowder_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AUG_DesertHex.BP_UG_Skin_AUG_DesertHex_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AUG_Woodland.BP_UG_Skin_AUG_Woodland_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_AKM.BP_Firearm_AKM_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AKM_BearClaw.BP_UG_Skin_AKM_BearClaw_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AKM_Chrome.BP_UG_Skin_AKM_Chrome_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AKM_RedDark.BP_UG_Skin_AKM_RedDark_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AKM_RustWrap.BP_UG_Skin_AKM_RustWrap_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_L85A2.BP_Firearm_L85A2_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_L85_TrueGrit.BP_UG_Skin_L85_TrueGrit_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_M16A4.BP_Firearm_M16A4_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M16A4_DesertHex.BP_UG_Skin_M16A4_DesertHex_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M16A4_UniversalDigital.BP_UG_Skin_M16A4_UniversalDigital_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M16A4_Veteran.BP_UG_Skin_M16A4_Veteran_C",
    ],
    '/Game/Game/Actors/Weapons/MachineGun/BP_Firearm_PKM.BP_Firearm_PKM_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_PKM_RustWrap.BP_UG_Skin_PKM_RustWrap_C",
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_MK14.BP_Firearm_MK14_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MK14_Hunter.BP_UG_Skin_MK14_Hunter_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MK14_NocturneBlue.BP_UG_Skin_MK14_NocturneBlue_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MK14_TwitchGreen.BP_UG_Skin_MK14_TwitchGreen_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MK14_Veteran.BP_UG_Skin_MK14_Veteran_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_HBadger.BP_Firearm_HBadger_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_HoneyBadger_BlackPowder.BP_UG_Skin_HoneyBadger_BlackPowder_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_HoneyBadger_NocturneBlue.BP_UG_Skin_HoneyBadger_NocturneBlue_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_HoneyBadger_Woodland.BP_UG_Skin_HoneyBadger_Woodland_C",
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_SG552.BP_Firearm_SG552_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_SG552_RustWrap.BP_UG_Skin_SG552_RustWrap_C"
    ],
    '/Game/Game/Actors/Weapons/SubMachineGun/BP_Firearm_UZI.BP_Firearm_UZI_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_UZI_Damascus.BP_UG_Skin_UZI_Damascus_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_UZI_UrbanDigital.BP_UG_Skin_UZI_UrbanDigital_C"
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_AKS74u.BP_Firearm_AKS74u_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AKS74u_RustWrap.BP_UG_Skin_AKS74u_RustWrap_C"
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_Famas.BP_Firearm_Famas_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_FAMAS_Carbon.BP_UG_Skin_FAMAS_Carbon_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_FAMAS_UrbanDigital.BP_UG_Skin_FAMAS_UrbanDigital_C"
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_VHS.BP_Firearm_VHS_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_VHS_TwoTone.BP_UG_Skin_VHS_TwoTone_C"
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_QTS11.BP_Firearm_QTS11_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_QTS11_UniversalDigital.BP_UG_Skin_QTS11_UniversalDigital_C"
    ],
    '/Game/Game/Actors/Weapons/SubMachineGun/BP_Firearm_Sterling.BP_Firearm_Sterling_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Sterling_BearClaw.BP_UG_Skin_Sterling_BearClaw_C"
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_G36K.BP_Firearm_G36K_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_G36_TrueGrit.BP_UG_Skin_G36_TrueGrit_C"
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_G36_DigitalSplatter.BP_UG_Skin_G36_DigitalSplatter_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_Tariq.BP_Firearm_Tariq_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Tariq_Woodland.BP_UG_Skin_Tariq_Woodland_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_L105.BP_Firearm_L105_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_L105_UniversalDigital.BP_UG_Skin_L105_UniversalDigital_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_M1911.BP_Firearm_M1911_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M1911_UrbanDigital.BP_UG_Skin_M1911_UrbanDigital_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_M45.BP_Firearm_M45_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M45_BlackPowder.BP_UG_Skin_M45_BlackPowder_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M45_DesertHex.BP_UG_Skin_M45_DesertHex_C"
    ],
     '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_M9.BP_Firearm_M9_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M9_RedDark.BP_UG_Skin_M9_RedDark_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_PF940.BP_Firearm_PF940_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_PF940_NocturneBlue.BP_UG_Skin_PF940_NocturneBlue_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_PF940_TwoTone.BP_UG_Skin_PF940_TwoTone_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_PF940_TwitchGreen.BP_UG_Skin_PF940_TwitchGreen_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_BrowningHP.BP_Firearm_BrowningHP_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Browning_Carbon.BP_UG_Skin_Browning_Carbon_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_MR73.BP_Firearm_MR73_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MR73_TrueGrit.BP_UG_Skin_MR73_TrueGrit_C"
    ],
    '/Game/Game/Actors/Weapons/SideArm/BP_Firearm_DesertEagle.BP_Firearm_DesertEagle_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Deagle_BearClaw.BP_UG_Skin_Deagle_BearClaw_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Deagle_Chrome.BP_UG_Skin_Deagle_Chrome_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Deagle_Damascus.BP_UG_Skin_Deagle_Damascus_C"
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_SKS.BP_Firearm_SKS_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_SKS_BearClaw.BP_UG_Skin_SKS_BearClaw_C"
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_AKAlpha.BP_Firearm_AKAlpha_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AlphaAK_Carbon.BP_UG_Skin_AlphaAK_Carbon_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AlphaAK_UrbanDigital.BP_UG_Skin_AlphaAK_UrbanDigital_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_AlphaAK_Whiteout.BP_UG_Skin_AlphaAK_Whiteout_C"
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_ACE52.BP_Firearm_ACE52_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_ACE52_UrbanDigital.BP_UG_Skin_ACE52_UrbanDigital_C"
    ],
    '/Game/Game/Actors/Weapons/SubMachineGun/BP_Firearm_P90.BP_Firearm_P90_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_P90_Chrome.BP_UG_Skin_P90_Chrome_C"
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_Tavor.BP_Firearm_Tavor_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Tavor7_BlackPowder.BP_UG_Skin_Tavor7_BlackPowder_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Tavor7_DesertHex.BP_UG_Skin_Tavor7_DesertHex_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Tavor7_Woodland.BP_UG_Skin_Tavor7_Woodland_C"
    ],
    '/Game/Game/Actors/Weapons/SubMachineGun/BP_Firearm_Vector.BP_Firearm_Vector_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Vector_TwoTone.BP_UG_Skin_Vector_TwoTone_C"
    ],
    '/Game/Game/Actors/Weapons/SubMachineGun/BP_Firearm_GreaseGun.BP_Firearm_GreaseGun_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_GreaseGun_TrueGrit.BP_UG_Skin_GreaseGun_TrueGrit_C"
    ],
    '/Game/Game/Actors/Weapons/Shotgun/BP_Firearm_KS23.BP_Firearm_KS23_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_KS23_Carbon.BP_UG_Skin_KS23_Carbon_C"
    ],
    '/Game/Game/Actors/Weapons/Shotgun/BP_Firearm_M870.BP_Firearm_M870_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M870_NocturneBlue.BP_UG_Skin_M870_NocturneBlue_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M870_TrueGrit.BP_UG_Skin_M870_TrueGrit_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M870_TwoTone.BP_UG_Skin_M870_TwoTone_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M870_TwitchGreen.BP_UG_Skin_M870_TwitchGreen_C"
    ],
    '/Game/Game/Actors/Weapons/Shotgun/BP_Firearm_TOZ.BP_Firearm_TOZ_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_TOZ_BearClaw.BP_UG_Skin_TOZ_BearClaw_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_TOZ_Chrome.BP_UG_Skin_TOZ_Chrome_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_TOZ_RedDark.BP_UG_Skin_TOZ_RedDark_C"
    ],
    '/Game/Game/Actors/Weapons/SubMachineGun/BP_Firearm_MP5A2.BP_Firearm_MP5A2_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MP5A2_Chrome.BP_UG_Skin_MP5A2_Chrome_C"
    ],
    '/Game/Game/Actors/Weapons/Shotgun/BP_Firearm_KSG.BP_Firearm_KSG_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_KSG_Woodland.BP_UG_Skin_KSG_Woodland_C"
    ],
    '/Game/Game/Actors/Weapons/SubMachineGun/BP_Firearm_MP7.BP_Firearm_MP7_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MP7_DesertHex.BP_UG_Skin_MP7_DesertHex_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MP7_TwoTone.BP_UG_Skin_MP7_TwoTone_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_MP7_TwitchGreen.BP_UG_Skin_MP7_TwitchGreen_C"
    ],
    '/Game/Game/Actors/Weapons/AssaultRifle/BP_Firearm_ASVAL.BP_Firearm_ASVAL_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_ASVAL_Carbon.BP_UG_Skin_ASVAL_Carbon_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_ASVAL_RedDark.BP_UG_Skin_ASVAL_RedDark_C"
    ],
    '/Game/Game/Actors/Weapons/MachineGun/BP_Firearm_M249.BP_Firearm_M249_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M249_Veteran.BP_UG_Skin_M249_Veteran_C"
    ],
    '/Game/Game/Actors/Weapons/MachineGun/BP_Firearm_M60.BP_Firearm_M60_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M60_BlackPowder.BP_UG_Skin_M60_BlackPowder_C"
    ],
    '/Game/Game/Actors/Weapons/MachineGun/BP_Firearm_RPK.BP_Firearm_RPK_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_RPK_Damascus.BP_UG_Skin_RPK_Damascus_C"
    ],
    '/Game/Game/Actors/Weapons/SniperRifle/BP_Firearm_M24.BP_Firearm_M24_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M24_Hunter.BP_UG_Skin_M24_Hunter_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M24_TrueGrit.BP_UG_Skin_M24_TrueGrit_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M24_Veteran.BP_UG_Skin_M24_Veteran_C"
    ],
    '/Game/Game/Actors/Weapons/SniperRifle/BP_Firearm_Mosin.BP_Firearm_Mosin_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Mosin_BearClaw.BP_UG_Skin_Mosin_BearClaw_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_Mosin_RustWrap.BP_UG_Skin_Mosin_RustWrap_C"
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_M1Garand.BP_Firearm_M1Garand_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M1Garand_Whiteout.BP_UG_Skin_M1Garand_Whiteout_C"
    ],
    '/Game/Game/Actors/Weapons/AntiMaterial/BP_Firearm_M82.BP_Firearm_M82_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M82_Hunter.BP_UG_Skin_M82_Hunter_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M82_UniversalDigital.BP_UG_Skin_M82_UniversalDigital_C"
    ],
    '/Game/Game/Actors/Weapons/AntiMaterial/BP_Firearm_M99.BP_Firearm_M99_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M99_Whiteout.BP_UG_Skin_M99_Whiteout_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M99_Damascus.BP_UG_Skin_M99_Damascus_C"
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_M110.BP_Firearm_M110_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M110_BlackPowder.BP_UG_Skin_M110_BlackPowder_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M110_Hunter.BP_UG_Skin_M110_Hunter_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_M110_Woodland.BP_UG_Skin_M110_Woodland_C"
    ],
    '/Game/Game/Actors/Weapons/BattleRifle/BP_Firearm_SVD.BP_Firearm_SVD_C': [
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_SVD_Carbon.BP_UG_Skin_SVD_Carbon_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_SVD_RedDark.BP_UG_Skin_SVD_RedDark_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_SVD_RustWrap.BP_UG_Skin_SVD_RustWrap_C",
        "/Game/Game/Actors/Weapons/Upgrades/Skins/BP_UG_Skin_SVD_Whiteout.BP_UG_Skin_SVD_Whiteout_C"
    ],
}
class SkinSelector:
    def __init__(self, root, available_skins, json_data):
        self.root = root
        self.available_skins = available_skins
        self.json_data = json_data
        self.weapon_comboboxes = {}
        self.weapon_labels = []
        
        self.initialize_gui()
        
    def initialize_gui(self):
        ttk.Label(self.root, text="Select Class:").pack(pady=10)
        self.class_combobox = ttk.Combobox(self.root, values=list(self.json_data['playerClasses'].keys()))
        max_length = max([len(val) for val in self.json_data['playerClasses'].keys()])
        self.class_combobox['width'] = max_length

        self.class_combobox.pack(pady=10)
        self.class_combobox.bind("<<ComboboxSelected>>", self.update_presets)

        ttk.Label(self.root, text="Select Preset:").pack(pady=10)
        self.preset_combobox = ttk.Combobox(self.root)
        self.preset_combobox.pack(pady=10)
        self.preset_combobox.bind("<<ComboboxSelected>>", self.update_weapons)

        ttk.Button(self.root, text="Save Skins", command=self.save_skins).pack(pady=20)

    def update_presets(self, event):
        selected_class = self.class_combobox.get()
        presets = ['default', 'nightDefault'] + [preset['presetName'] for preset in self.json_data['playerClasses'][selected_class]['presets']]
        self.preset_combobox['values'] = presets
        self.preset_combobox.set('')  # Clear current selection

    def update_weapons(self, event):
        # Clear existing weapon dropdowns and labels
        for weapon, combobox in self.weapon_comboboxes.items():
            combobox.destroy()
        self.weapon_comboboxes.clear()
        
        for label in self.weapon_labels:
            label.destroy()
        self.weapon_labels.clear()

        selected_class = self.class_combobox.get()
        selected_preset = self.preset_combobox.get()
        if selected_preset in ['default', 'nightDefault']:
            preset_data = self.json_data['playerClasses'][selected_class][selected_preset]
        else:
            preset_data = next(preset for preset in self.json_data['playerClasses'][selected_class]['presets'] if preset['presetName'] == selected_preset)
        
        for item in preset_data['items']:
            weapon = item['item']
            if weapon in self.available_skins:
                label = ttk.Label(self.root, text=f"Select skin for {weapon.split('/')[-1]}:")
                label.pack(pady=10)
                self.weapon_labels.append(label)
                
                combobox = ttk.Combobox(self.root, values=[skin.split('/')[-1].split('.')[-2] for skin in self.available_skins[weapon]])
                combobox.pack(pady=10)
                combobox.set(next((upgrade.split('/')[-1].split('.')[-2] for upgrade in item['upgrades'] if 'Skins' in upgrade), ''))
                self.weapon_comboboxes[weapon] = combobox

        # Load skins right after updating weapon dropdowns
        self.load_skins()

    def load_skins(self):
        selected_class = self.class_combobox.get()
        selected_preset = self.preset_combobox.get()
    
        # Fetch the preset data based on selected class and preset
        if selected_preset in ['default', 'nightDefault']:
            preset_data = self.json_data['playerClasses'][selected_class][selected_preset]
        else:
            preset_data = next(preset for preset in self.json_data['playerClasses'][selected_class]['presets'] if preset['presetName'] == selected_preset)
    
        # Load the skins for each weapon in the preset
        for item in preset_data['items']:
            weapon = item['item']
            if weapon in self.weapon_comboboxes:
                self.weapon_comboboxes[weapon].set(next((upgrade.split('/')[-1].split('.')[-2] for upgrade in item['upgrades'] if 'Skins' in upgrade), ''))

    def save_skins(self):
        selected_class = self.class_combobox.get()
        selected_preset = self.preset_combobox.get()
    
        # Determine if the selected preset is 'default', 'nightDefault', or a custom preset
        if selected_preset in ['default', 'nightDefault']:
            preset_data = self.json_data['playerClasses'][selected_class][selected_preset]
        else:
            preset_data = next(preset for preset in self.json_data['playerClasses'][selected_class]['presets'] if preset['presetName'] == selected_preset)
    
        # Update the skins for each weapon in the preset
        # Update the skins for each weapon in the preset
        for item in preset_data['items']:
            weapon = item['item']
            if weapon in self.weapon_comboboxes:
                # Filter out existing skins from upgrades
                item['upgrades'] = [upgrade for upgrade in item['upgrades'] if 'Skins' not in upgrade]
                
                # Add the selected skin to upgrades
                selected_skin_suffix = self.weapon_comboboxes[weapon].get()
                for skin in self.available_skins[weapon]:
                    if selected_skin_suffix in skin:
                        selected_skin = skin
                        break
                else:
                    print(f"Couldn't match skin for suffix: {selected_skin_suffix}")
                    print(f"Available skins: {self.available_skins[weapon]}")
                    continue


                if not selected_skin:
                    print(f"Warning: Couldn't find a matching skin for weapon {weapon} with suffix {selected_skin_suffix}")
                    print(f"Available skins for {weapon}: {self.available_skins[weapon]}")
                    continue

                item['upgrades'].append(selected_skin)

    
        # Save the modified JSON data back to the file
        file_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Insurgency', 'Saved', 'SaveGames', 'SteamProfile', 'Theater.json')
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.json_data, file, ensure_ascii=False, indent=4)


# Load the JSON data
file_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Insurgency', 'Saved', 'SaveGames', 'SteamProfile', 'Theater.json')
with open(file_path, 'r', encoding='utf-8') as file:
    theater_data = json.load(file)

root = tk.Tk()
app = SkinSelector(root, available_skins, theater_data)
root.mainloop()
