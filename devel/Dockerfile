FROM knspar/phronetis:0.1.44
RUN apt update -y && apt  install -y libcap2-bin && \
   setcap 'cap_net_raw,cap_net_admin=+eip' /usr/bin/justniffer && \
   apt install -y curl && \
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
   chmod +x kubectl  && \
   mv kubectl /usr/local/bin/ 
   