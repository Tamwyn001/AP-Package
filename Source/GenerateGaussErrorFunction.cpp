#include <iostream>
#include <fstream>
#include <math.h>

#define M_PI       3.14159265358979323846   // pi

//we have t \ in [0, 5] and delta_t = 0,01
const int total_value = 50000;
const double delta_t = 0.0001;

struct Data{
    double x;
    double y;
};


Data values[2 * total_value]; //from - 5 to 5 is 2*5

Data gauss_at_point(double x)
{
    Data out;
    out.x = x;
    out.y = exp(-x*x / 2);
    return out;
}

int find_value_in_interval(const int start, const int end, const double to_find, Data datas[])
{
    double last_value= -HUGE_VAL;
    double value; 
    for(int i = 0; i < 2 * total_value; i++)
    {
        value = datas[i].x;
        if (value >= to_find && last_value <= to_find )
        {
            return i;
        }
        last_value = value;
    }
    std::cout<<"Index not found for value: "<< to_find << " from " << start << " to " << end << "\n";
    return 0;
}

double integrate(double a, double b, Data datas[])
{
    double sum = 0.;
    //find start and end index
    int i;
    int id_start;
    int id_end;
    bool found_a;

    id_start = find_value_in_interval(0, total_value, a, datas);
    id_end = find_value_in_interval(id_start, total_value, b, datas);

    for (i = id_start; i <= id_end; i++ )
    {
        sum += datas[i].y * delta_t;
    }
    return sum;
}

void write_to_file(Data output_datas[])
{
    std::ofstream file("C:\\Users\\Tamwyn\\Documents\\Physik\\AP\\Source\\AP Package\\ProbaGaussIn.dat"
                    ,std::ios::trunc);
    for(int i = 0; i < total_value; i++)
    {
        file<<output_datas[i].x << " " << output_datas[i].y << "\n";
       // std::cout << output_datas[i].x << " " << output_datas[i].y << "\n";
    }
    return;
}

int main(int argc, char* argv[])
{
    Data proba[total_value];
    int i;
    for(i = 0; i < 2 * total_value; i++)
    {
        values[i] = gauss_at_point((i - total_value) * delta_t);
    }
    i = 0;

    for (double t = 0.; t < 5.; t += delta_t)
    {
        proba[i].x = t;
        proba[i].y = (1/sqrt(2*M_PI))*integrate(-t, t, values);
        i++;
    }

    write_to_file(proba);

    return 0;   
}