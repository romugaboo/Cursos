using System;
using bytebank;
using bytebank.Titular;

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Seja bem vinde ao banco da lari!\n");
        ContaCorrente conta1 = new (123, "110123 - X");
        conta1.Titular.Nome = "André Silva";
        conta1.NomeAgencia = "Agência Central";
        conta1.Saldo = 100;

        ContaCorrente conta2 = new(456, "292910 - Y");
        conta2.Titular.Nome = "Larissa Coelho";
        conta2.NomeAgencia = "Agência Filial";
        conta2.Saldo = 450;

        Console.WriteLine("Saldo da Larissa pré-transferência: " + conta2.Saldo);
        Console.WriteLine("Saldo do André pré-transferência: " + conta1.Saldo);
        bool transferencia = conta1.Transferir(50, conta2);
        Console.WriteLine("Transferência realizada com sucesso? "+ transferencia);
        Console.WriteLine("Saldo da Larissa pós-transferência: " + conta2.Saldo);
        Console.WriteLine("Saldo do André pós-transferência: " + conta1.Saldo);

        Cliente sarah = new Cliente();
        sarah.Nome = "Sarah Silva";
        sarah.Profissao = "Professora";
        sarah.Cpf = "11111111-12";

        Cliente ester = new Cliente();
        ester.Nome = "Ester Almeida";
        ester.Profissao = "Advogada";
        ester.Cpf = "868524125-32";

        ContaCorrente contaAndre = new ContaCorrente(159,"152869-x");
        contaAndre.Titular.Nome = " André Pereira";
        contaAndre.Titular.Profissao = "Auxiliar Administrativo";
        contaAndre.Saldo = 100;

        Console.WriteLine("Total de clientes: " + Cliente.TotalClientesCadastrados);

        Console.ReadKey();
    }
}