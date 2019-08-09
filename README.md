# UNMANNED VEHICLES.

> ## Basic Messaging Programs in C using ZMQ

> ### weather station server program

```c
#include "zhelpers.h"
#include <unistd.h>
#include <stdlib.h>

int main (int argc, char **argv)
{
	// prepare the context and publisher
	void *context = zmq_ctx_new ();
	void *publisher = zmq_socket (context, ZMQ_PUB);
	int rc = zmq_bind (publisher, "tcp://*:5556");

	assert (rc == 0);

	rc = zmq_bind (publisher, "ipc://weather.ipc");
	assert (rc == 0);

	// Initialize the random number generator
	srandom ((unsigned) time (NULL));

	while (1)
	{
		int zipcode, temperature, relhumidity;
		zipcode = randof (1000000);
		temperature = randof (251) - 80;
		relhumidity = randof (50) + 10;

		// send messages to all subscribers
		char update[20];
		sprintf (update, "%05d %d %d", zipcode, temperature, relhumidity);

		s_send (publisher, update);
	}

	zmq_close (publisher);
	zmq_ctx_destroy (context);

	return 0;
}
```

> ### weather station client program

```c
#include "zhelpers.h"
#include <unistd.h>

int main (int argc, char **argv)
{
	void *context = zmq_ctx_new ();

	printf("Collecting updates from weather station\n");
	void *subscriber = zmq_socket (context, ZMQ_SUB);
	int rc = zmq_connect (subscriber, "tcp://localhost:5556");

	// subscriber to zipcode
	char *filter = "10001";
	rc = zmq_setsockopt (subscriber, ZMQ_SUBSCRIBE, filter, strlen (filter));
	assert (rc == 0);

	// Process 100 updates
	int update_nbr;
	long total_temp = 0;
	// for (update_nbr = 0; update_nbr < 100; update_nbr ++)
	while (1)
	{
		char *string = s_recv (subscriber);
		int zipcode, temperature, relhumidity;
		sscanf (string, "%d %d %d", &zipcode, &temperature, &relhumidity);
		printf ("Temperature = %d\n", temperature);
		total_temp = total_temp + temperature;
		free (string);
	}

	printf ("Average temperature of zipcode was %d ", (int)(total_temp / update_nbr));
	zmq_close (subscriber);
	zmq_ctx_destroy (context);

	return 0;
}
```




  
| TITLE  | INFO  |  LINK |
|---|---|---|
| ACRONYMS  |  Some of acronyms used in UV | [Link](/pages/env-setup/acronyms.md)  |
| Environment (HW)  | Hardware setup part  |  [Link](/pages/env-setup/envsetuphw.md) |
| Environment (Software)  |  Software setup part | [Link](/pages/env-setup/envsetup.md)  |

