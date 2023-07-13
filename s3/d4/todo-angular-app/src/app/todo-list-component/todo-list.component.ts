// import { Component } from '@angular/core';

// @Component({
//   selector: 'app-todo-list-component',
//   templateUrl: './todo-list-component.component.html',
//   styleUrls: ['./todo-list-component.component.css']
// })
// export class TodoListComponentComponent {

// }


import { Component } from '@angular/core';
import { Todo } from '../todo.interface';
import { TodoService } from '../todo.service';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})

export class TodoListComponent {
  todos: Todo[];

  constructor(private todoService: TodoService) {
    this.todos = todoService.getTodos();
  }

  completeTodo(todo: Todo): void {
    this.todoService.updateTodoCompletion(todo, true);
  }

  deleteTodo(todo: Todo): void {
    this.todoService.deleteTodo(todo);
  }
}

