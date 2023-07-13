import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.css']
})
export class CounterComponent {
  count: number = 0;

  increment(){
    this.count++
  }
  decrement(){
    if(this.count === 0){
      alert("count is zero!")
   }else{
     this.count--
   }
   
  }

  checkoutCount(){
    if(this.count === 0){
      const decrementButtton = document.getElementById(
        'decrementBtn'
      ) as HTMLButtonElement;
      decrementButtton.disabled = true;
    }else{
      const decrementButtton = document.getElementById(
        'decrementBtn'
      ) as HTMLButtonElement;
      decrementButtton.disabled = false;
    }
  }
}
