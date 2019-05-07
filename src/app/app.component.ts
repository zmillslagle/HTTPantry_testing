import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
    hasImage: boolean = false;
    isLoading: boolean = false;
    time: number = 0;
    interval;
    fileURL: string = 'http://127.0.0.1:5002/';

    startTimer() {
        this.interval = setInterval(() => {
            this.time++;
        },10)
    }
    
    pauseTimer() {
        clearInterval(this.interval);
    }

    showImage() {
        this.hasImage = !this.hasImage;
        this.startTimer()
        this.isLoading = true;
    }

    imageLoad() {
        this.isLoading = false;
        this.pauseTimer()
    }
}
