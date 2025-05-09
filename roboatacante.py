def get_ball_position():
    data, _ = vision_sock.recvfrom(4096)
    packet = SSL_WrapperPacket()
    packet.ParseFromString(data)
    if packet.detection.balls:
        ball = packet.detection.balls[0]
        return ball.x / 1000, ball.y / 1000  # Convertendo mm para m
    return None

def follow_ball():
    kp = 1.0  
    while True:
        robot_pos = get_robot_position()
        ball_pos = get_ball_position()
        if robot_pos and ball_pos:
            rx, ry, rtheta = robot_pos
            bx, by = ball_pos
            
            # Erro de posição
            dx = bx - rx
            dy = by - ry
            distance = (dx**2 + dy**2)**0.5
            
            # Velocidades proporcionais
            vx = kp * dx
            vy = kp * dy
            w = 0  
            
            # Limita velocidades
            max_speed = 1.0
            if distance > max_speed:
                vx *= max_speed / distance
                vy *= max_speed / distance
            
            send_robot_velocity(vx, vy, w)
        time.sleep(0.05)

# Executa
follow_ball()