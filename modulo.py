import socket
import time
from proto.ssl_vision_wrapper_pb2 import SSL_WrapperPacket
from proto.grsim_commands_pb2 import grSim_Robot_Command
from proto.grsim_packet_pb2 import grSim_Packet

VISION_IP = "224.5.23.2"  # Endereço multicast do grSim
VISION_PORT = 10020
vision_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
vision_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
vision_sock.bind((VISION_IP, VISION_PORT))

# Configuração do socket UDP para comandos
COMMAND_IP = "127.0.0.1"  # IP local do grSim
COMMAND_PORT = 20011
command_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_robot_position():
    data, _ = vision_sock.recvfrom(4096)
    packet = SSL_WrapperPacket()
    packet.ParseFromString(data)
    for robot in packet.detection.robots_yellow:  # Assumindo robô amarelo
        if robot.robot_id == 0:  # ID do robô
            return robot.x / 1000, robot.y / 1000, robot.orientation  # Convertendo mm para m
    return None

def send_robot_velocity(vx, vy, w):
    packet = grSim_Packet()
    cmd = packet.commands.robots_commands.add()
    cmd.id = 0  # ID do robô
    cmd.yellowteam = True  # Time amarelo
    cmd.veltangent = vx  # Velocidade em x
    cmd.velnormal = vy   # Velocidade em y
    cmd.velangular = w   # Velocidade angular
    command_sock.sendto(packet.SerializeToString(), (COMMAND_IP, COMMAND_PORT))

# Teste
while True:
    pos = get_robot_position()
    if pos:
        print(f"Posição: x={pos[0]:.2f}, y={pos[1]:.2f}, theta={pos[2]:.2f}")
    send_robot_velocity(0.5, 0, 0)  # Move para frente a 0.5 m/s
    time.sleep(0.1)