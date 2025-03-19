public class Iphone implements AparelhoTelefonico, NavegadorWeb, ReprodutorMusica{
    // Telefone
    private NavegadorWeb web;
    private AparelhoTelefonico tel;
    private ReprodutorMusica music;

    public void tocar(){
        System.out.println("Musica tocando");
    }
    public void pausar(){
        System.out.println("Musica pausada");
    }
    public void selecionarMusica(){
        System.out.println("Musica selecionada");
    }
    public void exibirPagina(){
        System.out.println("Exibindo Pagina...");
    }
    public void adicionarNovaAba(){
        System.out.println("Abrindo nova aba...");
    }
    public void atualizarPagina(){
        System.out.println("Atualizando pagina. Aguarde...");
    }
    public void ligar(){
        System.out.println("Discando");
    }
    public void atender(){
        System.out.println("Alô?!");
    }
    public void iniciarCorreioVoz(){
        System.out.println("Abrindo Correio de voz...");
    }
}
