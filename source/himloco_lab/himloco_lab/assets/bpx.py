# Copyright (c) 2024-2026 Ziqi Fan
# SPDX-License-Identifier: Apache-2.0

"""Configuration
"""

import isaaclab.sim as sim_utils
from isaaclab.actuators import DCMotorCfg, ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

# from robot_lab.assets import ISAACLAB_ASSETS_DATA_DIR

YTM_BPX_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=False,
        merge_fixed_joints=True,
        replace_cylinders_with_capsules=False,
        asset_path=f"/root/himloco_lab/source/himloco_lab/data/Robots/bpx/bpx_description/urdf/bpx.urdf",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
        joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
            gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.38),
        # joint_pos={
        #     ".*L_hip_joint": 0.0,
        #     ".*R_hip_joint": -0.0,
        #     "F.*_thigh_joint": 0.8,
        #     "R.*_thigh_joint": 0.8,
        #     ".*_calf_joint": -1.5,
        # },
        joint_pos={
            ".*_hip_roll_joint": 0.0,
            ".*_hip_pitch_joint": 0.8,
            ".*_knee_joint": -1.5,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": DCMotorCfg(
            joint_names_expr=[".*"],
            effort_limit=30.0,
            saturation_effort=30.0,
            velocity_limit=20.0,
            stiffness=45.0,
            damping=1.2,
            friction=0.0,
        ),
    },
)
"""Configuration of BPX using DC motor.
"""