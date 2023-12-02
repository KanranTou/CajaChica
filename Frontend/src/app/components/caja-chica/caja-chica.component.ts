import { Component, OnInit } from '@angular/core';
import { ConexionService } from 'src/app/services/conexion.service';

@Component({
  selector: 'app-caja-chica',
  templateUrl: './caja-chica.component.html',
  styleUrls: ['./caja-chica.component.css'],
})
export class CajaChicaComponent implements OnInit {
  cajasChicas: any[] = []; // Arreglo para almacenar las cajas chicas

  constructor(private cajaChicaService: ConexionService) { }

  ngOnInit(): void {
    this.obtenerCajasChicas();
  }

  obtenerCajasChicas(): void {
    this.cajaChicaService.obtenerTodasCajasChicas().subscribe(
      (cajasChicas) => {
        this.cajasChicas = cajasChicas;
      },
      (error) => {
        console.error('Error al obtener cajas chicas:', error);
      }
    );
  }
}