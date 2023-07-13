// import { Component } from '@angular/core';

// @Component({
//   selector: 'app-todo-item-component',
//   templateUrl: './todo-item-component.component.html',
//   styleUrls: ['./todo-item-component.component.css']
// })
// export class TodoItemComponentComponent {

// }

import { Component, Input } from '@angular/core';
import { Todo } from '../todo.interface';

@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  styleUrls: ['./todo-item.component.css']
})

export class TodoItemComponent {
  @Input() todo!: Todo;

  completeTodo(): void {
    // Invoke the completeTodo method of TodoListComponent passing the current todo
  }

  deleteTodo(): void {
    // Invoke the deleteTodo method of TodoListComponent passing the current todo
  }
}
