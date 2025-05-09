#include <iostream>
#include <string>

class Carro {
private:
    int vel;
    int freio;
    int aceleracao;
    std::string modelo;
    std::string marca;
    int ano;
    int id;
   int pedido;
    int itens;
     int valor;
    int valorT;
      

public:
int Fisico;
    int Juridico;
    int Cliente;  
    Carro(std::string marca, std::string modelo, int ano, int vel = 0, int freio = 0, int aceleracao = 0 , int fisico, int juridico, int cliente )
        : marca(marca), modelo(modelo), ano(ano), vel(vel), freio(freio), aceleracao(aceleracao), Fisico(Fisico), Juridico(Juridico) {}

    virtual void fazersom() {
        std::cout << "O Carro está funcionando.\n" << std::endl;
    }

    virtual void imprimirDados() {
        std::cout << "Marca: " << marca << "\nModelo: " << modelo << "\nAno: " << ano << "\n";
        std::cout << "Velocidade: " << vel << "\nFreio: " << freio << "\nAceleracao: " << aceleracao << "\n";
    }

    void acelera(int incremento) {
        vel += incremento;
    }

    // Getters
    std::string getMarca() const { return marca; }
    std::string getModelo() const { return modelo; }
    int getAno() const { return ano; }
    int getVel() const { return vel; }
    int getFreio() const { return freio; }
    int getAceleracao() const { return aceleracao; }

    // Setters
    void setVel(int v) { vel = v; }
    void setFreio(int f) { freio = f; }
    void setAceleracao(int a) { aceleracao = a; }
};

class Moto : public Carro {
private:
    int bau;
    int cilindradas;
    int marchas;

public:
    Moto(std::string marca, std::string modelo, int ano, int vel = 0, int freio = 0, int aceleracao = 0,
         int bau = 0, int cilindradas = 0, int marchas = 0)
        : Carro(marca, modelo, ano, vel, freio, aceleracao), bau(bau), cilindradas(cilindradas), marchas(marchas) {}

    void fazersom() override {
        std::cout << "A Moto está funcionando.\n" << std::endl;
    }

    void imprimirDados() override {
        Carro::imprimirDados();
        std::cout << "Bau: " << bau << "\nCilindradas: " << cilindradas << "\nMarchas: " << marchas << "\n";
    }

    int getBau() const { return bau; }
    int getCilindradas() const { return cilindradas; }
    int getMarchas() const { return marchas; }
};

class Caminhao : public Carro {
private:
    int carga;
    int peso;

public:
    Caminhao(std::string marca, std::string modelo, int ano, int vel = 0, int freio = 0, int aceleracao = 0,
             int carga = 0, int peso = 0)
        : Carro(marca, modelo, ano, vel, freio, aceleracao), carga(carga), peso(peso) {}

    void fazersom() override {
        std::cout << "O Caminhao está funcionando.\n" << std::endl;
    }

    void imprimirDados() override {
        Carro::imprimirDados();
        std::cout << "Carga: " << carga << "\nPeso: " << peso << "\n";
    }

    // Getters specific to Caminhao
    int getCarga() const { return carga; }
    int getPeso() const { return peso; }
};

class Pedido : public Carro {

private:

 int id;
 std::string nome;
 int pedido;
 int itens;
 int valor;
 int valorT;

 public:
Pedido(int id, std::string nome, int pedido, int itens, int valorT)
    : Carro("", "", 0), id(id), nome(nome), pedido(pedido), itens(itens), valorT(valorT) {}



// Métodos Get
int get_id() const { return id; }
std::string get_nome() const { return nome; }
int get_pedido() const {return pedido;}
int get_itens() const {return itens;}
int get_valorT() const {return valorT;}

// Métodos Set
void set_id(int id) { this->id = id;}
void set_nome(std::string nome) {  this->id = id;}
void set_pedido(int pedido) {this->pedido = pedido;}
void set_itens(int itens)  { this->itens = itens;}
void set_valorT(int valorT)  {  this->valorT = valorT; }
};


class Cliente : public Carro {
public:

    Cliente(int Juridico, int Fisico, Cliente c()) 
 : Cliente("" , "", 0), Juridico(Juridico), Fisico() {}
    Cliente() {
        std::cout << "Sou um cliente\n";
    }
};


int main() {



   
    
   

    Cliente c;
    Cliente* a0 = new Cliente("Fisico", "350R$");
    Cliente* a1 = new Cliente("Juridico", "1500R$");

      
    Carro* a1 = new Carro("Toyota", "Corolla", 2020);
    Caminhao* a2 = new Caminhao("Honda", "Civic", 2019, 0, 0, 0, 10000, 5000);
    Moto* a3 = new Moto("Ford", "Focus", 2018, 0, 0, 0, 1, 600, 6);



     enum Tipocliente {
JURIDICO,
FISICO
}
    switch (Tipocliente) {

         case 1:
    if  (Tipocliente  == JURIDICO){
std::cout << "1 - Juridico" << std::endl;
        break;
    }
    case 2:

     if (Tipocliente == FISICO){
         std::cout << "2 - Fisico" << std::endl;

         break;    
    
    }

     std::cout << "Agora escolha o seu veiculo" << std::endl;
     a0->imprimirDados();

     

    std::cout << "Carro 1:\n";
    a1->imprimirDados();
    a1->fazersom();

    std::cout << "Caminhao 2:\n";
    a2->imprimirDados();
    a2->fazersom();

    std::cout << "Moto 3:\n";
    a3->imprimirDados();
    a3->fazersom();

    std::cout << "\nMenu de Interacao:\n";
    std::cout << "Carro 1:\n";
    std::cout << "Marca: " << a1->getMarca() << "\n";
    std::cout << "Modelo: " << a1->getModelo() << "\n";

    std::cout << "Caminhao 2:\n";
    std::cout << "Marca: " << a2->getMarca() << "\n";
    std::cout << "Modelo: " << a2->getModelo() << "\n";
    std::cout << "Carga: " << a2->getCarga() << "\n";
    std::cout << "Peso: " << a2->getPeso() << "\n";

    std::cout << "Moto 3:\n";
    std::cout << "Marca: " << a3->getMarca() << "\n";
    std::cout << "Modelo: " << a3->getModelo() << "\n";
    std::cout << "Marchas: " << a3->getMarchas() << "\n";
    std::cout << "Cilindradas: " << a3->getCilindradas() << "\n";
     

    delete a0;
    delete a1;
    delete a2;
    delete a3;
   




    return 0;
}
};