public class Main {
    public static void main(String[] args) {
        /*int num = 7;
        double num2 = 10.8;
        String nome = "Adriel";

        System.out.println("Bem vindo, "+nome+"!");

        if (num > 10){
            System.out.println("Maior que 10!");
        }
        else {
            System.out.println("Menor que 10!");
        }

        for(int i = 0; i < 10; i++){
            System.out.println(i);
        }*/

        Carro carro_1 = new Carro("Fiat","Uno","Amarelo","PQP-0131",1992);
        Carro carro_2 = new Carro("Ferrari","465","Vermelha","BBQ-0000",2017);
        Carro carro_3 = new Carro("BMW","328i","Branco","PAS-2391",2020);
        Carro carro_4 = new Carro("Lamborghini","Gallardo","Preto","IDW-1241",2009);
        carro_1.imprimir();
        carro_2.imprimir();
        //carro_1.marca = "Fiat";
        //carro_1.setMarca("Fiat");
        //carro_1.modelo = "Uno";
        //carro_1.setModelo("Uno");
        //carro_1.cor = "Amarelo";
        //carro_1.setCor("Amarelo");
        //carro_1.placa = "PQP-0131";
        //carro_1.setPlaca("PQP-0131");
        //carro_1.ano = 1992;
        //carro_1.setAno(1992);
        //carro_1.ligado = false;
        System.out.println(carro_1.getMarca());

        //System.out.println("O carro da marca "+carro_1.marca+" e modelo "+carro_1.modelo+" , é do ano de "+carro_1.ano+" e possuí a placa "+carro_1.placa+".");
        carro_1.ligar();
        //carro_1.desligar();
        carro_1.acelerar();
        carro_1.drift();

    }
}