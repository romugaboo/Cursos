import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) {
        ContaTerminal contaTerminal = new ContaTerminal();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o número da conta:");
        contaTerminal.setNumero(scanner.nextInt());
        scanner.nextLine();

        System.out.println("Digite a agência:");
        contaTerminal.setAgencia(scanner.nextLine());

        System.out.println("Digite o seu nome:");
        contaTerminal.setNomeCliente(scanner.nextLine());

        System.out.println("Digite o saldo disponível para saque");
        contaTerminal.setSaldo(scanner.nextInt());
        scanner.nextLine();

        System.out.println("Olá " + contaTerminal.getNomeCliente() + ", obrigado por criar uma conta em nosso banco, " +
                "sua agência é " + contaTerminal.getAgencia() + ", conta " + contaTerminal.getNumero() + " e " +
                "seu " + "saldo " + contaTerminal.getSaldo() + " já está disponível para saque.");

    }
    public int numero;
    private String agencia;
    private String nomeCliente;
    private int saldo;
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }
    public String getAgencia() {
        return agencia;
    }
    public void setAgencia(String agencia) {
        this.agencia = agencia;
    }
    public String getNomeCliente() {
        return nomeCliente;
    }
    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }
    public int getSaldo() {
        return saldo;
    }
    public void setSaldo(int saldo) {
        this.saldo = saldo;
    }
}


