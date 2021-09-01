import rospy

from dynamic_reconfigure.server import Server
from dynamic_parameters.cfg import paramsConfig

def callback(config, level):
    #print("Kp = ", config.Kp, "\tKi = ", config.Ki, "\tKd = ", config.Kd)
    rospy.set_param('LQR', [config.N_max, config.min_dist, config.rc_max,config.rc_min])


    return config

if __name__ == "__main__":
    rospy.init_node("pid_parameters", anonymous = False)   # Node name will appear in the GUI

    srv = Server(paramsConfig, callback)

    rospy.spin()