public class CommandLineArguments {

    public static void main(String[] args) {

        if(args.length >= 2){

            System.out.println("First Argument : " + args[0]);
            System.out.println("Second Argument : " + args[1]);

        }else{

            System.out.println("Please pass two command line arguments.");

        }

    }
}