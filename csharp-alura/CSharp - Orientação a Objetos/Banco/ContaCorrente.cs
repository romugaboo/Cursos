using bytebank.Titular;

namespace bytebank
{
    public class ContaCorrente
    {
        public Cliente Titular = new Cliente();
        public string NomeAgencia { get; set; }

        private int _numeroAgencia;
        public int NumeroAgencia
        {
            get
            {
                return _numeroAgencia;
            }
            set
            {
                if (value <= 0)
                    Console.WriteLine("Não é possível inserir saldo negativo");
                else
                    _numeroAgencia = value;
            }
        }

        private string _conta;
        public string Conta
        {
            get
            {
                return _conta;
            }
            set
            {
                if (value == null)
                    return;
                else
                    _conta = value;
            }
        }

        private double saldo;
        public double Saldo
        {
            get
            {
                return saldo;
            }
            set
            {
                if (value < 0)
                    return;
                else
                    saldo = value;
            }
        }

        public bool Sacar(double valor)
        {
            if (saldo < valor)
                return false;

            if (valor < 0)
                return false;

            else
            {
                saldo -= valor;
                return true;
            }
        }

        public void Depositar(double valor)
        {
            if (valor < 0)
                return;
            saldo += valor;
        }

        public bool Transferir(double valor, ContaCorrente destino)
        {
            if (saldo < valor)
                return false;

            if (valor < 0)
                return false;

            else
            {
                saldo -= valor;
                destino.saldo += valor;
                return true;
            }
        }

        public ContaCorrente(int _numeroAgencia, string conta)
        {
            NumeroAgencia = _numeroAgencia;
            Conta = conta;
            TotalDeContasCriadas += 1;
        }
        public static int TotalDeContasCriadas { get; set; }
    }
}