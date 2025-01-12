import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpService } from "./http.service"
import { AppComponent } from './app.component';
import { HttpClientModule} from "@angular/common/http"
import { FormsModule } from '@angular/forms';
import { VesoComponent } from './veso/veso.component'; // <-- import FormsModule.

@NgModule({
  declarations: [
    AppComponent,
    VesoComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
