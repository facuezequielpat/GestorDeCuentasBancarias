drop database if exists banco;
create database banco;
use banco;



create table persona(
	dni int primary key,
    nombre varchar(20),
    apellido varchar(20)
    
);

create table dep_ret(
	id_dep_ret int  ,
    deposito float,
    retiro float,
    saldo float,
    dni_dep_ret int ,
    fechaIngreso datetime 
);

create table bitacoraTrigger(
	id_bitacora int primary key not null auto_increment,
    fecha datetime not null ,
    consulta_hecha varchar(2000) not null 
);



alter table dep_ret
add foreign key (id_dep_ret)
references bitacoraTrigger  (id_bitacora);

alter table dep_ret
add foreign key (dni_dep_ret)
references persona(dni);




drop trigger if exists after_insert_dep_ret;
DELIMITER $$

create trigger after_insert_dep_ret# Quiere decir 'crear disparador'
after insert on dep_ret # Quiere decir 'Despues inserta en persona'
for each row # Quiere decir "Por cada registro"

begin 
    DECLARE nombre VARCHAR(20);
    DECLARE apellido VARCHAR(20);
    
    SELECT p.nombre, p.apellido INTO nombre, apellido FROM persona p WHERE dni = NEW.dni_dep_ret;
    
    INSERT INTO bitacoraTrigger (fecha, consulta_hecha) VALUES (NOW(), CONCAT('Registro: dni: ', NEW.dni_dep_ret, ' nombre: ', nombre, ' apellido: ', apellido, ' deposito: '
    , NEW.deposito, ' retiro: ', NEW.retiro, ' saldo: ', NEW.saldo));
    
    
end;
$$
DELIMITER ; 



drop trigger if exists after_update_dep_ret $$
DELIMITER $$

create trigger after_update_dep_ret
after update on dep_ret
for each row

begin 
    DECLARE nombre VARCHAR(20);
    DECLARE apellido VARCHAR(20);
    
    SELECT p.nombre, p.apellido INTO nombre, apellido FROM persona p WHERE dni = NEW.dni_dep_ret;
    
    
    
    INSERT INTO bitacoraTrigger (fecha, consulta_hecha) VALUES (NOW(), CONCAT('Modificacion: dni: ', NEW.dni_dep_ret,' nombre: ', nombre ,' apellido: ',apellido,' deposito: '
    , NEW.deposito, ' retiro: ', NEW.retiro, ' saldo: ', NEW.saldo));
end;
$$
DELIMITER ; 

drop trigger if exists after_delete_dep_ret;
DELIMITER $$
create trigger after_delete_dep_ret
after delete on dep_ret
for each row

begin 
    DECLARE nombre VARCHAR(20);
    DECLARE apellido VARCHAR(20);
    DECLARE dni int;
    
    SELECT p.nombre, p.apellido, p.dni INTO nombre, apellido, dni 
    FROM persona p 
    WHERE p.dni = OLD.dni_dep_ret;
    
    INSERT INTO bitacoraTrigger (fecha, consulta_hecha) VALUES (
        NOW(),
        CONCAT('Borrado: dni: ', OLD.dni_dep_ret, ' nombre: ', nombre, ' apellido: ', apellido, ' deposito: ',
        OLD.deposito, ' retiro: ', OLD.retiro, ' saldo: ', OLD.saldo)
        
    );
end;
$$
DELIMITER ;





