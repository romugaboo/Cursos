import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Iphone iphone = new Iphone();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ligando Iphone...");
        System.out.println("Selecione o que deseja fazer: \n");
        System.out.println("1 - App Telefone\n2 - App Web\n3 - App Musica\n4 - Sair");

        Integer opc = scanner.nextInt();

        while (opc != 4) {
            if (opc.equals(1)) {
                System.out.println("1 - Atender Chamada\n2 - Discar\n3 - Correio de voz\n4 - Sair");
                Integer subopc = scanner.nextInt(); ;

                while (subopc != 4) {
                    if (subopc.equals(1)) {
                        iphone.atender();
                    } else if (subopc.equals(2)) {
                        iphone.ligar();
                    } else if (subopc.equals(3)) {
                        iphone.iniciarCorreioVoz();
                    } else {
                        System.out.println("Insira um valor valido");
                    }
                    System.out.println("1 - Atender Chamada\n2 - Discar\n3 - Correio de voz\n4 - Sair");
                    subopc = scanner.nextInt(); ;
                }
            } else if (opc.equals(2)) {
                System.out.println("1 - Exibir página\n2 - Adicionar nova aba\n3 - Atualizar página\n4 - Sair");
                Integer subopc = scanner.nextInt();

                while (subopc != 4) {
                    if (subopc.equals(1)) {
                        iphone.exibirPagina();
                    } else if (subopc.equals(2)) {
                        iphone.adicionarNovaAba();
                    } else if (subopc.equals(3)) {
                        iphone.atualizarPagina();
                    } else {
                        System.out.println("Insira um valor valido");
                    }
                    System.out.println("1 - Exibir página\n2 - Adicionar nova aba\n3 - Atualizar página\n4 - Sair");
                    subopc = scanner.nextInt();
                }
            } else if (opc.equals(3)) {
                System.out.println("1 - Tocar múcica\n2 - Pausar música\n3 - Selecionar música\n4 - Sair");
                Integer subopc = scanner.nextInt(); ;

                while (subopc != 4) {
                    if (subopc.equals(1)) {
                        iphone.tocar();
                    } else if (subopc.equals(2)) {
                        iphone.pausar();
                    } else if (subopc.equals(3)) {
                        iphone.selecionarMusica();
                    } else {
                        System.out.println("Insira um valor valido");
                    }
                    System.out.println("1 - Tocar múcica\n2 - Pausar música\n3 - Selecionar música\n4 - Sair");
                    subopc = scanner.nextInt(); ;
                }
            }
            System.out.println("1 - Menu Telefone\n2 - Menu Web\n3 - Menu Musica\n4 - Sair");
            opc = scanner.nextInt();
        }
        scanner.close();
        System.out.println("Desligando Iphone...");
    }
}