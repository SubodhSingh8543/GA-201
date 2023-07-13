// import { Component } from '@angular/core';

// @Component({
//   selector: 'app-create-todo-component',
//   templateUrl: './create-todo-component.component.html',
//   styleUrls: ['./create-todo-component.component.css']
// })
// export class CreateTodoComponentComponent {

// }

import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Todo } from '../todo.interface';
import { TodoService } from '../todo.service';

@Component({
  selector: 'app-create-todo',
  templateUrl: './create-todo.component.html',
  styleUrls: ['./create-todo.component.css']
})

export class CreateTodoComponent {
  constructor(private todoService: TodoService) { }

  createTodo(form: NgForm): void {
    const todo: Todo = {
      id: Date.now(),
      title: form.value.title,
      description: form.value.description,
      completed: false
    };

    this.todoService.addTodo(todo);
    form.resetForm();
  }
}
