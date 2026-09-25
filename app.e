Start.TaskManagerApp
       System.output:
              Print("=================================");
              Print("     E-LANGUAGE TASK MANAGER     ");
              Print("=================================");

       // 1. Initialize a dynamic vector list with your first two tasks
       var.list(MyTasks) = (CodeInterpreter, PushToGitHub)

       System.output:
              Print("Current task count in your tracker list:", MyTasks.length);
              Print("Task position 0:", MyTasks.position0);
              Print("Task position 1:", MyTasks.position1);
              Print("---------------------------------");

       // 2. Interactively prompt user input for a new task item
       var(newTask) = (Syntax).System.input("Enter a new task to add to your list:" , (String.input))

       // 3. Dynamically append your new item to the active array list frame
       MyTasks.append(newTask);

       System.output:
              Print("---------------------------------");
              Print("Updated task count inside your list:", MyTasks.length);
              Print("Newly appended task item is stored at index position 2:", MyTasks.position2);

       // 4. Dump your updated data payload onto your Mac's hard drive
       System.output:
              Print("Saving task data stream down into a file asset...");

       System.file.write("todo_export.txt", (newTask));

       System.output:
              Print("Operation complete. Verification file saved as todo_export.txt");
End.TaskManagerApp
