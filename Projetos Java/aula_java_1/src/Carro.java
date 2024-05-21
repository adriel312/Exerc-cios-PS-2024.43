public class Carro {
    public String marca;
    public String modelo;
    public String cor;
    public String placa;
    protected int ano;
    private boolean ligado;

    public Carro(String marca, String modelo, String cor, String placa, int ano) {
        setMarca(marca);
        setModelo(modelo);
        setCor(cor);
        setPlaca(placa);
        setAno(ano);
        setLigado(false);
    }
    public void imprimir(){
        System.out.println("Meu carro é da marca " + marca+ " e modelo " + modelo + " com a cor " + cor + "do ano " + ano);
    }
    public void ligar(){
        if (ligado == false) {
            //ligado = true;
            setLigado(true);
            System.out.println("O carro foi ligado!");
        }
        else{
            System.out.println("ERRO.O carro já estava ligado!");
        }
    }
    public void desligar(){
        if (ligado == true){
            //ligado = false;
            setLigado(false);
            System.out.println("O carro foi desligado!");
        }
        else {
            System.out.println("O carro já estava desligado!");
        }
    }
    public void drift(){
        if (ligado == true){
            System.out.println("Vruuuuuuuum, psispispsipsi");
        }
        else {
            System.out.println("O carro está desligado!");
        }
    }
    public void acelerar(){
        if (ligado == true){
            System.out.println("Vruuuuuum!");
        }
        else {
            System.out.println("O carro está desligado!");
        }
    }
    public void passar_marcha(){
        System.out.println("Passamos a marcha!");
    }
    public void ligar_farol(){
        System.out.println("Os faróis foram ligados!");
    }

    public void setMarca(String marca){
        this.marca = marca;
    }
    public String getMarca(){
        return this.marca;
    }
    public void setModelo(String modelo){
        this.modelo = modelo;
    }
    public String getModelo(){
        return this.modelo;
    }
    public void setCor(String cor){
        this.cor = cor;
    }
    public String getCor(){
        return this.cor;
    }
    public void setPlaca(String placa){
        this.placa = placa;
    }
    public String getPlaca(){
        return this.placa;
    }
    public void setAno(int ano){
        this.ano = ano;
    }
    public int getAno(){
        return this.ano;
    }
    private void setLigado(boolean ligado){
        this.ligado = ligado;
    }
    public boolean getLigado(){
        return this.ligado;
    }
}
