<template>
    <div>
        <header class="text-gray-600 body-font">
            <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
                <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
                    <span class="ml-3 text-xl">
                        <NuxtLink :to="{ name: 'index' }">
                            Logo
                        </NuxtLink>
                    </span>
                </a>
                <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center list-none">

                    <li class="mr-5 hover:text-gray-900">
                        <NuxtLink :to="{ name: 'index' }">
                            Home page
                        </NuxtLink>
                    </li>
                    <li class="mr-5 hover:text-gray-900">
                        <NuxtLink :to="{ name: 'posts' }">
                            Posts page
                        </NuxtLink>
                    </li>
                </nav>
                <button
                    class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Button
                    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        class="w-4 h-4 ml-1" viewBox="0 0 24 24">
                        <path d="M5 12h14M12 5l7 7-7 7"></path>
                    </svg>
                </button>
            </div>
        </header>
    </div>
</template>